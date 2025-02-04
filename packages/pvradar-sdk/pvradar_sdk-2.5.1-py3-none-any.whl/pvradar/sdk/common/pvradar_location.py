from pvlib.location import Location as PvlibLocation
from timezonefinder import TimezoneFinder
from debugpy.common.singleton import Singleton


class TZFinder(TimezoneFinder, Singleton):
    pass


class PvradarLocation(PvlibLocation):
    def __init__(self, latitude, longitude, tz=None, altitude=None, name=None):
        if tz is None:
            tz = TZFinder().timezone_at(lng=longitude, lat=latitude)
        if tz is None:
            raise ValueError('Could not determine timezone')
        super().__init__(latitude, longitude, tz=tz, altitude=altitude, name=name)
