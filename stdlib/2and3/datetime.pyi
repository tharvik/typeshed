# Stubs for datetime

#import sys
from time import struct_time
from typing import (
    Hashable, Optional, SupportsAbs, Tuple,
    overload,
)

#_T = TypeVar('_T', None, timedelta)

MINYEAR = ...  # type: int
MAXYEAR = ...  # type: int

class date(Hashable):
    min = ...  # type: date
    max = ...  # type: date
    resolution = ...  # type: timedelta
    def __init__(self, year: int, month: int, day: int) -> None: ...
    @classmethod
    def today(cls) -> date: ...
    @classmethod
    def fromtimestamp(cls, timestamp: float) -> date: ...
    @classmethod
    def fromordinal(cls, ordinal: int) -> date: ...
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
#    def __le__(self, other: date) -> bool: ...
    def __lt__(self, other: date) -> bool: ...
#    def __ge__(self, other: date) -> bool: ...
#    def __gt__(self, other: date) -> bool: ...
    def __add__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: date) -> timedelta: ...
    def __hash__(self) -> int: ...
    def replace(self, year: int = ..., month: int = ..., day: int = ...) -> date: ...
    def timetuple(self) -> struct_time: ...
    def toordinal(self) -> int: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    def isocalendar(self) -> Tuple[int, int, int]: ...
    def isoformat(self) -> str: ...
    def ctime(self) -> str: ...
    def strftime(self, fmt: str) -> str: ...
    def __format__(self, fmt: str) -> str: ...

class time: ...
#    min = ...  # type: time
#    max = ...  # type: time
#    resolution = ...  # type: timedelta

#    def __init__(self, hour: int = ..., minute: int = ..., second: int = ..., microsecond: int = ...,
#                 tzinfo: tzinfo = ...) -> None: ...

#    @property
#    def hour(self) -> int: ...
#    @property
#    def minute(self) -> int: ...
#    @property
#    def second(self) -> int: ...
#    @property
#    def microsecond(self) -> int: ...
#    @property
#    def tzinfo(self) -> _tzinfo: ...

#    def __le__(self, other: time) -> bool: ...
#    def __lt__(self, other: time) -> bool: ...
#    def __ge__(self, other: time) -> bool: ...
#    def __gt__(self, other: time) -> bool: ...
#    def __hash__(self) -> int: ...
#    def isoformat(self) -> str: ...
#    def strftime(self, fmt: str) -> str: ...
#    def __format__(self, fmt: str) -> str: ...  def utcoffset(self) -> Optional[int]: ...
#    def tzname(self) -> Optional[str]: ...
#    def dst(self) -> Optional[int]: ...
#    def replace(self, hour: int = ..., minute: int = ..., second: int = ...,
#                microsecond: int = ..., tzinfo: Union[_tzinfo, bool] = ...) -> time: ...

# TODO replace when mypy#1775
_tzinfo = tzinfo
_date = date
_time = time

class datetime(Hashable):
    min = ...  # type: datetime
    max = ...  # type: datetime
    resolution = ...  # type: timedelta
    def __init__(self, year: int, month: int, day: int, hour: int = ...,
                 minute: int = ..., second: int = ..., microsecond: int = ...,
                 tzinfo: Optional[tzinfo] = ...) -> None: ...
    @classmethod
    def today(cls) -> datetime: ...
    @classmethod
    def now(cls, tz: Optional[tzinfo] = ...) -> datetime: ...
    @classmethod
    def utcnow(cls) -> datetime: ...
    @classmethod
    def fromtimestamp(cls, timestamp: float,
                      tz: Optional[timezone] = ...) -> datetime: ...
    @classmethod
    def utcfromtimestamp(cls, timestamp: float) -> datetime: ...
    @classmethod
    def fromordinal(cls, ordinal: int) -> datetime: ...
    @classmethod
    def combine(cls, date: date, time: time) -> datetime: ...
    @classmethod
    def strptime(cls, date_string: str, format: str) -> datetime: ...
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> Optional[_tzinfo]: ...
    def __add__(self, other: timedelta) -> datetime: ...
    @overload
    def __sub__(self, other: timedelta) -> datetime: ...
    @overload
    def __sub__(self, other: datetime) -> timedelta: ...
    def __lt__(self, other: datetime) -> bool: ...
#    def __le__(self, other: datetime) -> bool: ...
#    def __ge__(self, other: datetime) -> bool: ...
#    def __gt__(self, other: datetime) -> bool: ...
    def __hash__(self) -> int: ...
    def date(self) -> _date: ...
    def time(self) -> _time: ...
    def timetz(self) -> _time: ...
    def replace(self, year: int = ..., month: int = ..., day: int = ..., hour: int = ...,
                minute: int = ..., second: int = ..., microsecond: int = ..., tzinfo:
                Optional[_tzinfo] = ...) -> datetime: ...
    def astimezone(self, tz: Optional[_tzinfo] = ...) -> datetime: ...
    def utcoffset(self) -> Optional[int]: ...
    def dst(self) -> Optional[int]: ...
    def tzname(self) -> Optional[str]: ...
    def timetuple(self) -> struct_time: ...
    def utctimetuple(self) -> struct_time: ...
    def toordinal(self) -> int: ...
    def timestamp(self) -> float: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    def isocalendar(self) -> Tuple[int, int, int]: ...
    def isoformat(self, sep: str = ...) -> str: ...
    def ctime(self) -> str: ...
    def strftime(self, format: str) -> str: ...
    def __format__(self, format: str) -> str: ...

class timedelta(Hashable, SupportsAbs[timedelta]):
    min = ...  # type: timedelta
    max = ...  # type: timedelta
    resolution = ...  # type: timedelta
    def __init__(self, days: float = ..., seconds: float = ..., microseconds: float = ...,
                 milliseconds: float = ..., minutes: float = ..., hours: float = ...,
                 weeks: float = ...) -> None: ...
    @property
    def days(self) -> int: ...
    @property
    def seconds(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    def __add__(self, other: timedelta) -> timedelta: ...
    def __sub__(self, other: timedelta) -> timedelta: ...
    def __mul__(self, other: float) -> timedelta: ...
    def __rmul__(self, other: float) -> timedelta: ...
    @overload
    def __truediv__(self, other: timedelta) -> float: ...
    @overload
    def __truediv__(self, other: float) -> timedelta: ...
    @overload
    def __floordiv__(self, other: timedelta) -> int: ...
    @overload
    def __floordiv__(self, other: int) -> timedelta: ...
    def __mod__(self, other: timedelta) -> timedelta: ...
    def __divmod__(self, other: timedelta) -> Tuple[int, timedelta]: ...
    def __pos__(self) -> timedelta: ...
    def __neg__(self) -> timedelta: ...
    def __abs__(self) -> timedelta: ...
#    def __le__(self, other: timedelta) -> bool: ...
#    def __lt__(self, other: timedelta) -> bool: ...
#    def __ge__(self, other: timedelta) -> bool: ...
#    def __gt__(self, other: timedelta) -> bool: ...
    def __hash__(self) -> int: ...
    def total_seconds(self) -> float: ...

class tzinfo: ...
#class tzinfo(object, Generic[_T]): ...
#    def tzname(self, dt: Optional[datetime]) -> str: ...
#    def utcoffset(self, dt: Optional[datetime]) -> _T: ...
#    def dst(self, dt: Optional[datetime]) -> _T: ...
#    def fromutc(self, dt: datetime) -> datetime: ...

class timezone(tzinfo): ...
#    utc = ...  # type: tzinfo
#    min = ...  # type: tzinfo
#    max = ...  # type: tzinfo

#    def __init__(self, offset: timedelta, name: str = ...) -> None: ...
#    def __hash__(self) -> int: ...
