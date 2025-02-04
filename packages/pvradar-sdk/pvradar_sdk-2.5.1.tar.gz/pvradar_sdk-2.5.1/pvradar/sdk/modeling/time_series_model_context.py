from datetime import tzinfo
from typing import Any, Optional
import pandas as pd
from .model_context import ModelContext
from ..common.pandas_utils import interval_to_index


def validate_timestamp_interval(value: pd.Interval) -> None:
    if (
        not isinstance(value, pd.Interval)
        or not isinstance(value.left, pd.Timestamp)
        or not isinstance(value.right, pd.Timestamp)
    ):
        raise ValueError('must be an Interval with pd.Timestamp endpoints')


def assert_equal_timezones(
    timezone1: tzinfo | str | None, timezone2: tzinfo | str | None, complaint: str = 'timezone offsets are not equal'
):
    now = pd.Timestamp('now')
    tzinfo1 = now.tz_localize(timezone1).tzinfo
    assert tzinfo1 is not None, 'invalid timezone1 string'
    tzinfo2 = now.tz_localize(timezone2).tzinfo
    assert tzinfo2 is not None, 'invalid timezone2 string'
    assert tzinfo1.utcoffset(now) == tzinfo2.utcoffset(now), complaint


def maybe_adjust_tz(value: pd.Interval, default_tz: Any) -> pd.Interval:
    if default_tz is None:
        raise ValueError('default_tz must be set')
    if value.left.tzinfo is None:
        new_left = pd.Timestamp(value.left, tz=default_tz)
    else:
        assert_equal_timezones(value.left.tzinfo, default_tz, 'interval.left timezone is not equal to default_tz')
        new_left = value.left
    if value.right.tzinfo is None:
        new_right = pd.Timestamp(value.right, tz=default_tz)
    else:
        assert_equal_timezones(value.right.tzinfo, default_tz, 'interval.right timezone is not equal to default_tz')
        new_right = value.right
    return pd.Interval(new_left, new_right)


class TimeSeriesModelContext(ModelContext):
    def __init__(self, *, interval: Optional[pd.Interval] = None, default_tz: Any = 'UTC', **kwargs) -> None:
        super().__init__(**kwargs)
        self.default_tz = default_tz
        if interval:
            self.interval = interval

    @property
    def interval(self) -> pd.Interval:
        return self.resource('interval')

    @interval.setter
    def interval(self, value: pd.Interval) -> None:
        validate_timestamp_interval(value)
        value = maybe_adjust_tz(value, self.default_tz)
        self['interval'] = value

    def timestamps(self, freq: str = '1h') -> pd.DatetimeIndex:
        return interval_to_index(self.interval, freq)
