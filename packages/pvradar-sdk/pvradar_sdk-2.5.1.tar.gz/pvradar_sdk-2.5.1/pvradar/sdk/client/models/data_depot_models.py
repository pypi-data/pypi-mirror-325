import pandas as pd

from ..api_query import Query
from ..client import PvradarClient
from pvlib.location import Location


def dd_precipitation_source_table(
    location: Location,
    interval: pd.Interval,
) -> pd.DataFrame:
    query = Query.from_site_environment(location=location, interval=interval)
    query['signal_names'] = 'precip_rate_total'
    query.set_path('dd-proxy/signals/available/csv')

    result = PvradarClient.instance().get_df(query)
    return result


def dd_precipitation(
    location: Location,
    interval: pd.Interval,
) -> pd.Series:
    query = Query.from_site_environment(location=location, interval=interval)
    query['signal_names'] = 'precip_rate_total'
    query.set_path('dd-proxy/signals/table/csv')

    table = PvradarClient.instance().get_df(query)
    series = table['precip']
    series.attrs['api_call'] = table['api_call']
    return series
