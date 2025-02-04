from typing import Any, Optional
from pvlib.location import Location
import pandas as pd

from ...common.pvradar_location import PvradarLocation
from ...modeling.basics import BindingNotFound, ModelParam
from ...modeling.model_context import ModelContext
from ...modeling.model_binder import AbstractBinder
from ..engine.engine_types import ModelContextLocator
from ..pvradar_site import PvradarSite
from ..client import PvradarClient
from ..api_query import Query
from ..platform.schemas import IAssembly, IProjectManifest
from .vtables import is_vtable, maybe_extend_df_with_dates, timed_vtable_to_df, vtable_to_df, is_timed_vtable
from .schemas import AssemblyName
from ..platform.technical_params_adaptor import make_site_design


def _remove_none_values(d: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}


class PvradarProjectBinder(AbstractBinder):
    def bind(
        self,
        *,
        resource_name: str,
        as_param: Optional[ModelParam] = None,
        defaults: Optional[dict[str, Any]] = None,
        context: Optional[ModelContext] = None,
    ) -> Any:
        assert isinstance(context, PvradarProject)
        if resource_name == 'design':
            tp = context.platform_technical_params_base
            context['design'] = make_site_design(tp['design'], context.location)
            return context['design']
        return BindingNotFound


class PvradarProject(PvradarSite):
    def __init__(
        self,
        project_id: str,
        *,
        default_variant_id: Optional[str] = '',
        interval: Optional[pd.Interval] = None,
    ) -> None:
        super().__init__(interval=interval)
        self['project_id'] = project_id
        self._default_variant_id = default_variant_id or 'wizard-no-cleaning'
        self._assembly_cache = {}
        self._client = PvradarClient.instance()
        self.binders.append(PvradarProjectBinder())

    def _make_cache_key(self, assembly_name: str, variant_id: str, **kwargs) -> str:
        non_empty = {k: v for k, v in kwargs.items() if v is not None}
        sorted_keys = sorted(non_empty.keys())
        result = f'{variant_id}/{assembly_name}'
        for key in sorted_keys:
            result += f'&{key}={non_empty[key]}'
        return result

    def _resolve_variant_id(self, variant_id: Optional[str]) -> str:
        return variant_id or self._default_variant_id

    def get_assembly(
        self,
        assembly_name: str,
        *,
        variant_id: Optional[str] = None,
        year_index: Optional[int] = None,
        step: Optional[int] = None,
    ):
        variant_id = self._resolve_variant_id(variant_id)
        kwargs = {
            'year_index': year_index,
            'step': step,
        }
        kwargs = _remove_none_values(kwargs)
        cache_key = self._make_cache_key(assembly_name, variant_id, **kwargs)
        if cache_key in self._assembly_cache:
            return self._assembly_cache[cache_key]
        assembly = self._fetch_assembly(assembly_name, variant_id, **kwargs)
        self._assembly_cache[cache_key] = assembly
        return assembly

    def _fetch_assembly(self, assembly_name: str, variant_id: str, **kwargs):
        dims = {}
        if 'year_index' in kwargs:
            dims['yearIndex'] = kwargs['year_index']
        if 'step' in kwargs:
            dims['step'] = kwargs['step']
        query = Query(project_id=self['project_id'], variant_id=variant_id, path=f'assemblies/{assembly_name}', params=dims)
        response = self._client.get_json(query)
        if 'meta' not in response:
            raise ValueError(f'Unexpected response: {response}')
        return response['meta']['result']

    def get_assembly_subject(
        self,
        assembly_name: AssemblyName,
        *,
        variant_id: Optional[str] = None,
        year_index: Optional[int] = None,
        step: Optional[int] = None,
    ) -> Any:
        assembly: IAssembly = self.get_assembly(
            assembly_name,
            variant_id=variant_id,
            year_index=year_index,
            step=step,
        )
        subject = assembly['subject']
        if is_timed_vtable(subject):
            tz = self.location.tz
            df = timed_vtable_to_df(subject, set_tz=tz)
            return df
        elif is_vtable(subject):
            df = vtable_to_df(subject)
            df = maybe_extend_df_with_dates(df)
            return df
        else:
            return subject

    @property
    def location(self) -> Location:
        if self.get('location') is None:
            m = self.platform_project_manifest
            self['location'] = PvradarLocation(latitude=m['location']['lat'], longitude=m['location']['lon'])
        return self['location']

    @location.setter
    def location(self, value: Optional[Location]) -> None:
        self['location'] = value

    def _fetch_and_cache_subject(self, assembly_name: AssemblyName, property_name: str = '') -> Any:
        if property_name == '':
            property_name = 'platform_' + assembly_name.replace('-', '_')
        if property_name in self:
            return self[property_name]
        self[property_name] = self.get_assembly_subject(assembly_name)
        return self[property_name]

    @property
    def platform_project_manifest(self) -> IProjectManifest:
        return self._fetch_and_cache_subject('project-manifest')

    @property
    def platform_technical_params_base(self) -> dict[str, Any]:
        return self._fetch_and_cache_subject('technical-params-base')

    @property
    def name(self) -> str:
        return self['project_id']

    @staticmethod
    def from_locator(locator: ModelContextLocator, tz: Optional[str] = None) -> PvradarSite:
        project_id = locator.get('project_id')
        if project_id is None:
            result = PvradarSite()
        else:
            result = PvradarProject(project_id=project_id, default_variant_id='wizard-snow-loss')
        if tz:
            result.default_tz = tz
            result.location.tz = tz
        return result
