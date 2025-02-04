from typing import Optional
import pandas as pd
from pvlib.location import Location
from .time_series_model_context import TimeSeriesModelContext


class GeoLocatedModelContext(TimeSeriesModelContext):
    def __init__(
        self,
        *,
        location: Optional[Location] = None,
        interval: Optional[pd.Interval] = None,
        **kwargs,
    ) -> None:
        if location:
            super().__init__(interval=interval, default_tz=location.tz, **kwargs)
            self.location = location
        else:
            super().__init__(interval=interval, **kwargs)

    @property
    def location(self) -> Location:
        return self['location']

    @location.setter
    def location(self, value: Optional[Location]) -> None:
        if value and not isinstance(value, Location):
            raise ValueError('location must be a Location object')
        if value and value.tz is not None:
            self.default_tz = value.tz
        self['location'] = value

    def copy(self) -> 'GeoLocatedModelContext':
        c = GeoLocatedModelContext()
        c.models = self.models.copy()
        c.binders = self.binders.copy()
        c._resources = self._resources.copy()
        c.default_tz = self.default_tz
        c.location = self.location
        c.interval = self.interval
        return c
