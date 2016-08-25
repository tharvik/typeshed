# Stubs for builtins (Python 3)

from typing import (
    TypeVar, Iterator, Iterable, overload,
    Sequence, MutableSequence, Mapping, MutableMapping, Tuple, List, Any, Dict, Callable, Generic,
    Set, AbstractSet, MutableSet, Sized, Reversible, SupportsInt, SupportsFloat, SupportsBytes,
    SupportsAbs, SupportsRound, IO, Union, ItemsView, KeysView, ValuesView, ByteString
)
from abc import abstractmethod, ABCMeta
from types import TracebackType
import numbers
import sys

# Note that names imported above are not automatically made visible via the
# implicit builtins import.

_T = TypeVar('_T')
_T_co = TypeVar('_T_co', covariant=True)
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_S = TypeVar('_S')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')

staticmethod = object() # Only valid as a decorator.
classmethod = object() # Only valid as a decorator.

class object:
    __doc__ = ...  # type: str
    __class__ = ...  # type: type
    __dict__ = ...  # type: Dict[str, Any]

    def __init__(self) -> None: ...
    def __new__(cls) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __eq__(self, o: object) -> bool: ...
    def __ne__(self, o: object) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...

class type:
    __bases__ = ...  # type: Tuple[type, ...]
    __name__ = ...  # type: str
    __qualname__ = ...  # type: str
    __module__ = ...  # type: str
    __dict__ = ...  # type: Dict[str, Any]
    __mro__ = ...  # type: Tuple[type, ...]

    @overload
    def __init__(self, o: object) -> None: ...
    @overload
    def __init__(self, name: str, bases: Tuple[type, ...], dict: Dict[str, Any]) -> None: ...
    @overload
    def __new__(cls, o: object) -> type: ...
    @overload
    def __new__(cls, name: str, bases: Tuple[type, ...], namespace: Dict[str, Any]) -> type: ...
    def __call__(self, *args: Any, **kwds: Any) -> Any: ...
    def __subclasses__(self) -> List[type]: ...
    # Note: the documentation doesnt specify what the return type is, the standard
    # implementation seems to be returning a list.
    def mro(self) -> List[type]: ...

class int(numbers.Integral):
    def __init__(self, x: Union[SupportsInt, str, bytes] = None, base: int = None) -> None: ...
    def bit_length(self) -> int: ...
    def to_bytes(self, length: int, byteorder: str, *, signed: bool = ...) -> bytes: ...
    @classmethod
    def from_bytes(cls, bytes: Sequence[int], byteorder: str, *,
                   signed: bool = ...) -> int: ...  # TODO buffer object argument

    def __add__(self, x: numbers.Integral) -> int: ...  # type: ignore
    def __sub__(self, x: int) -> int: ...
    def __mul__(self, x: numbers.Integral) -> int: ...  # type: ignore
    def __floordiv__(self, x: numbers.Integral) -> int: ...  # type: ignore
    def __truediv__(self, x: numbers.Integral) -> float: ...  # type: ignore
    def __mod__(self, x: numbers.Integral) -> int: ...  # type: ignore
    def __radd__(self, x: int) -> int: ...
    def __rsub__(self, x: int) -> int: ...
    def __rmul__(self, x: int) -> int: ...
    def __rfloordiv__(self, x: int) -> int: ...
    def __rtruediv__(self, x: int) -> float: ...
    def __rmod__(self, x: int) -> int: ...
    def __pow__(self, x: numbers.Integral) -> Any: ...  # Return type can be int or float, depending on x.  # type: ignore
    def __rpow__(self, x: int) -> Any: ...
    def __and__(self, n: numbers.Integral) -> int: ...  # type: ignore
    def __or__(self, n: numbers.Integral) -> int: ...  # type: ignore
    def __xor__(self, n: numbers.Integral) -> int: ...  # type: ignore
    def __lshift__(self, n: numbers.Integral) -> int: ...  # type: ignore
    def __rshift__(self, n: numbers.Integral) -> int: ...  # type: ignore
    def __rand__(self, n: int) -> int: ...
    def __ror__(self, n: int) -> int: ...
    def __rxor__(self, n: int) -> int: ...
    def __rlshift__(self, n: int) -> int: ...
    def __rrshift__(self, n: int) -> int: ...
    def __neg__(self) -> int: ...
    def __pos__(self) -> int: ...
    def __invert__(self) -> int: ...

    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __lt__(self, x: numbers.Integral) -> bool: ...  # type: ignore
    def __le__(self, x: numbers.Integral) -> bool: ...  # type: ignore
    def __gt__(self, x: numbers.Integral) -> bool: ...  # type: ignore
    def __ge__(self, x: numbers.Integral) -> bool: ...  # type: ignore

    def __str__(self) -> str: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: return self
    def __abs__(self) -> int: ...
    def __hash__(self) -> int: ...

class float(numbers.Real):
    def __init__(self, x: Union[SupportsFloat, str, bytes]=None) -> None: ...
    def as_integer_ratio(self) -> Tuple[int, int]: ...
    def hex(self) -> str: ...
    def is_integer(self) -> bool: ...
    @classmethod
    def fromhex(cls, s: str) -> float: ...

    def __add__(self, x: numbers.Real) -> float: ...  # type: ignore
    def __sub__(self, x: float) -> float: ...
    def __mul__(self, x: numbers.Real) -> float: ...  # type: ignore
    def __floordiv__(self, x: numbers.Real) -> float: ...  # type: ignore
    def __truediv__(self, x: numbers.Real) -> float: ...  # type: ignore
    def __mod__(self, x: numbers.Real) -> float: ...  # type: ignore
    def __pow__(self, x: numbers.Real) -> float: ...  # type: ignore
    def __radd__(self, x: float) -> float: ...
    def __rsub__(self, x: float) -> float: ...
    def __rmul__(self, x: float) -> float: ...
    def __rfloordiv__(self, x: float) -> float: ...
    def __rtruediv__(self, x: float) -> float: ...
    def __rmod__(self, x: float) -> float: ...
    def __rpow__(self, x: float) -> float: ...

    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __lt__(self, x: numbers.Real) -> bool: ...  # type: ignore
    def __le__(self, x: numbers.Real) -> bool: ...  # type: ignore
    def __gt__(self, x: numbers.Real) -> bool: ...  # type: ignore
    def __ge__(self, x: numbers.Real) -> bool: ...  # type: ignore
    def __neg__(self) -> float: ...
    def __pos__(self) -> float: ...

    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __abs__(self) -> float: ...
    def __hash__(self) -> int: ...

class complex(numbers.Complex):
    @overload
    def __init__(self, re: float = 0.0, im: float = 0.0) -> None: ...
    @overload
    def __init__(self, s: str) -> None: ...

    @property
    def real(self) -> float: ...
    @property
    def imag(self) -> float: ...

    def conjugate(self) -> complex: ...

    def __add__(self, x: numbers.Complex) -> complex: ...  # type: ignore
    def __sub__(self, x: complex) -> complex: ...
    def __mul__(self, x: numbers.Complex) -> complex: ...  # type: ignore
    def __pow__(self, x: numbers.Complex) -> complex: ...  # type: ignore
    def __truediv__(self, x: numbers.Complex) -> complex: ...  # type: ignore
    def __radd__(self, x: complex) -> complex: ...
    def __rsub__(self, x: complex) -> complex: ...
    def __rmul__(self, x: complex) -> complex: ...
    def __rpow__(self, x: complex) -> complex: ...
    def __rtruediv__(self, x: complex) -> complex: ...

    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __neg__(self) -> complex: ...
    def __pos__(self) -> complex: ...

    def __str__(self) -> str: ...
    def __abs__(self) -> float: ...
    def __hash__(self) -> int: ...

class str(Sequence[str]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, o: object) -> None: ...
    @overload
    def __init__(self, o: bytes, encoding: str = None, errors: str = 'strict') -> None: ...
    def capitalize(self) -> str: ...
    def center(self, width: int, fillchar: str = ' ') -> str: ...
    def count(self, x: str) -> int: ...
    def encode(self, encoding: str = 'utf-8', errors: str = 'strict') -> bytes: ...
    def endswith(self, suffix: Union[str, Tuple[str, ...]], start: int = None,
                 end: int = None) -> bool: ...
    def expandtabs(self, tabsize: int = 8) -> str: ...
    def find(self, sub: str, start: int = 0, end: int = 0) -> int: ...
    def format(self, *args: Any, **kwargs: Any) -> str: ...
    def format_map(self, map: Mapping[str, Any]) -> str: ...
    def index(self, sub: str, start: int = 0, end: int = 0) -> int: ...
    def isalnum(self) -> bool: ...
    def isalpha(self) -> bool: ...
    def isdecimal(self) -> bool: ...
    def isdigit(self) -> bool: ...
    def isidentifier(self) -> bool: ...
    def islower(self) -> bool: ...
    def isnumeric(self) -> bool: ...
    def isprintable(self) -> bool: ...
    def isspace(self) -> bool: ...
    def istitle(self) -> bool: ...
    def isupper(self) -> bool: ...
    def join(self, iterable: Iterable[str]) -> str: ...
    def ljust(self, width: int, fillchar: str = ' ') -> str: ...
    def lower(self) -> str: ...
    def lstrip(self, chars: str = None) -> str: ...
    def partition(self, sep: str) -> Tuple[str, str, str]: ...
    def replace(self, old: str, new: str, count: int = -1) -> str: ...
    def rfind(self, sub: str, start: int = 0, end: int = 0) -> int: ...
    def rindex(self, sub: str, start: int = 0, end: int = 0) -> int: ...
    def rjust(self, width: int, fillchar: str = ' ') -> str: ...
    def rpartition(self, sep: str) -> Tuple[str, str, str]: ...
    def rsplit(self, sep: str = None, maxsplit: int = -1) -> List[str]: ...
    def rstrip(self, chars: str = None) -> str: ...
    def split(self, sep: str = None, maxsplit: int = -1) -> List[str]: ...
    def splitlines(self, keepends: bool = ...) -> List[str]: ...
    def startswith(self, prefix: Union[str, Tuple[str, ...]], start: int = None,
                   end: int = None) -> bool: ...
    def strip(self, chars: str = None) -> str: ...
    def swapcase(self) -> str: ...
    def title(self) -> str: ...
    def translate(self, table: Dict[int, Any]) -> str: ...
    def upper(self) -> str: ...
    def zfill(self, width: int) -> str: ...
    @staticmethod
    @overload
    def maketrans(x: Union[Dict[int, Any], Dict[str, Any]]) -> Dict[int, Any]: ...
    @staticmethod
    @overload
    def maketrans(x: str, y: str, z: str = ...) -> Dict[int, Any]: ...

    def __getitem__(self, i: Union[int, slice]) -> str: ...
    def __add__(self, s: str) -> str: ...
    def __mul__(self, n: int) -> str: ...
    def __rmul__(self, n: int) -> str: ...
    def __mod__(self, *args: Any) -> str: ...
    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __lt__(self, x: str) -> bool: ...
    def __le__(self, x: str) -> bool: ...
    def __gt__(self, x: str) -> bool: ...
    def __ge__(self, x: str) -> bool: ...

    def __len__(self) -> int: ...
    def __contains__(self, s: object) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __str__(self) -> str: return self
    def __repr__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __hash__(self) -> int: ...

class bytes(ByteString):
    @overload
    def __init__(self, ints: Iterable[int]) -> None: ...
    @overload
    def __init__(self, string: str, encoding: str,
                 errors: str = 'strict') -> None: ...
    @overload
    def __init__(self, length: int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, o: SupportsBytes) -> None: ...
    def capitalize(self) -> bytes: ...
    def center(self, width: int, fillchar: bytes = None) -> bytes: ...
    def count(self, x: bytes) -> int: ...
    def decode(self, encoding: str = 'utf-8', errors: str = 'strict') -> str: ...
    def endswith(self, suffix: Union[bytes, Tuple[bytes, ...]]) -> bool: ...
    def expandtabs(self, tabsize: int = 8) -> bytes: ...
    def find(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def index(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def isalnum(self) -> bool: ...
    def isalpha(self) -> bool: ...
    def isdigit(self) -> bool: ...
    def islower(self) -> bool: ...
    def isspace(self) -> bool: ...
    def istitle(self) -> bool: ...
    def isupper(self) -> bool: ...
    def join(self, iterable: Iterable[bytes]) -> bytes: ...
    def ljust(self, width: int, fillchar: bytes = None) -> bytes: ...
    def lower(self) -> bytes: ...
    def lstrip(self, chars: bytes = None) -> bytes: ...
    def partition(self, sep: bytes) -> Tuple[bytes, bytes, bytes]: ...
    def replace(self, old: bytes, new: bytes, count: int = -1) -> bytes: ...
    def rfind(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def rindex(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def rjust(self, width: int, fillchar: bytes = None) -> bytes: ...
    def rpartition(self, sep: bytes) -> Tuple[bytes, bytes, bytes]: ...
    def rsplit(self, sep: bytes = None, maxsplit: int = -1) -> List[bytes]: ...
    def rstrip(self, chars: bytes = None) -> bytes: ...
    def split(self, sep: bytes = None, maxsplit: int = -1) -> List[bytes]: ...
    def splitlines(self, keepends: bool = ...) -> List[bytes]: ...
    def startswith(self, prefix: Union[bytes, Tuple[bytes, ...]]) -> bool: ...
    def strip(self, chars: bytes = None) -> bytes: ...
    def swapcase(self) -> bytes: ...
    def title(self) -> bytes: ...
    def translate(self, table: bytes, delete: bytes = None) -> bytes: ...
    def upper(self) -> bytes: ...
    def zfill(self, width: int) -> bytes: ...
    @classmethod
    def fromhex(cls, s: str) -> bytes: ...
    @classmethod
    def maketrans(cls, frm: bytes, to: bytes) -> bytes: ...

    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __hash__(self) -> int: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> bytes: ...
    def __add__(self, s: bytes) -> bytes: ...
    def __mul__(self, n: int) -> bytes: ...
    def __rmul__(self, n: int) -> bytes: ...
    def __contains__(self, o: object) -> bool: ...
    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __lt__(self, x: bytes) -> bool: ...
    def __le__(self, x: bytes) -> bool: ...
    def __gt__(self, x: bytes) -> bool: ...
    def __ge__(self, x: bytes) -> bool: ...

class bytearray(MutableSequence[int], ByteString):
    @overload
    def __init__(self, ints: Iterable[int]) -> None: ...
    @overload
    def __init__(self, string: str, encoding: str, errors: str = 'strict') -> None: ...
    @overload
    def __init__(self, length: int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def capitalize(self) -> bytearray: ...
    def center(self, width: int, fillchar: bytes = None) -> bytearray: ...
    def count(self, x: bytes) -> int: ...
    def decode(self, encoding: str = 'utf-8', errors: str = 'strict') -> str: ...
    def endswith(self, suffix: bytes) -> bool: ...
    def expandtabs(self, tabsize: int = 8) -> bytearray: ...
    def find(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def index(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def insert(self, index: int, object: int) -> None: ...
    def isalnum(self) -> bool: ...
    def isalpha(self) -> bool: ...
    def isdigit(self) -> bool: ...
    def islower(self) -> bool: ...
    def isspace(self) -> bool: ...
    def istitle(self) -> bool: ...
    def isupper(self) -> bool: ...
    def join(self, iterable: Iterable[bytes]) -> bytearray: ...
    def ljust(self, width: int, fillchar: bytes = None) -> bytearray: ...
    def lower(self) -> bytearray: ...
    def lstrip(self, chars: bytes = None) -> bytearray: ...
    def partition(self, sep: bytes) -> Tuple[bytearray, bytearray, bytearray]: ...
    def replace(self, old: bytes, new: bytes, count: int = -1) -> bytearray: ...
    def rfind(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def rindex(self, sub: bytes, start: int = 0, end: int = 0) -> int: ...
    def rjust(self, width: int, fillchar: bytes = None) -> bytearray: ...
    def rpartition(self, sep: bytes) -> Tuple[bytearray, bytearray, bytearray]: ...
    def rsplit(self, sep: bytes = None, maxsplit: int = -1) -> List[bytearray]: ...
    def rstrip(self, chars: bytes = None) -> bytearray: ...
    def split(self, sep: bytes = None, maxsplit: int = -1) -> List[bytearray]: ...
    def splitlines(self, keepends: bool = ...) -> List[bytearray]: ...
    def startswith(self, prefix: bytes) -> bool: ...
    def strip(self, chars: bytes = None) -> bytearray: ...
    def swapcase(self) -> bytearray: ...
    def title(self) -> bytearray: ...
    def translate(self, table: bytes, delete: bytes = None) -> bytearray: ...
    def upper(self) -> bytearray: ...
    def zfill(self, width: int) -> bytearray: ...
    @classmethod
    def fromhex(cls, s: str) -> bytearray: ...
    @classmethod
    def maketrans(cls, frm: bytes, to: bytes) -> bytes: ...

    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __hash__(self) -> int: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> bytearray: ...
    @overload
    def __setitem__(self, i: int, x: int) -> None: ...
    @overload
    def __setitem__(self, s: slice, x: Sequence[int]) -> None: ...
    def __delitem__(self, i: Union[int, slice]) -> None: ...
    def __add__(self, s: bytes) -> bytearray: ...
    def __iadd__(self, s: Iterable[int]) -> bytearray: ...
    def __mul__(self, n: int) -> bytearray: ...
    def __rmul__(self, n: int) -> bytearray: ...
    def __imul__(self, n: int) -> bytearray: ...
    def __contains__(self, o: object) -> bool: ...
    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __lt__(self, x: bytes) -> bool: ...
    def __le__(self, x: bytes) -> bool: ...
    def __gt__(self, x: bytes) -> bool: ...
    def __ge__(self, x: bytes) -> bool: ...

class memoryview():
    # TODO arg can be any obj supporting the buffer protocol
    def __init__(self, b: bytearray) -> None: ...

class bool(int, SupportsInt, SupportsFloat):
    def __init__(self, o: object = ...) -> None: ...

class slice:
    start = 0
    step = 0
    stop = 0
    def __init__(self, start: int, stop: int = 0, step: int = 0) -> None: ...

class tuple(Sequence[_T_co], Generic[_T_co]):
    def __init__(self, iterable: Iterable[_T_co] = ...) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @overload
    def __getitem__(self, x: int) -> _T_co: ...
    @overload
    def __getitem__(self, x: slice) -> Tuple[_T_co, ...]: ...
    def __iter__(self) -> Iterator[_T_co]: ...
    def __lt__(self, x: Tuple[_T_co, ...]) -> bool: ...
    def __le__(self, x: Tuple[_T_co, ...]) -> bool: ...
    def __gt__(self, x: Tuple[_T_co, ...]) -> bool: ...
    def __ge__(self, x: Tuple[_T_co, ...]) -> bool: ...
    def __add__(self, x: Tuple[_T_co, ...]) -> Tuple[_T_co, ...]: ...
    def __mul__(self, n: int) -> Tuple[_T_co, ...]: ...
    def __rmul__(self, n: int) -> Tuple[_T_co, ...]: ...
    def count(self, x: Any) -> int: ...
    def index(self, x: Any) -> int: ...

class function:
    # TODO not defined in builtins!
    __name__ = ...  # type: str
    __qualname__ = ...  # type: str
    __module__ = ...  # type: str
    __code__ = ... # type: Any

class list(MutableSequence[_T], Generic[_T]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> List[_T]: ...
    def append(self, object: _T) -> None: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def pop(self, index: int = -1) -> _T: ...
    def index(self, object: _T, start: int = 0, stop: int = ...) -> int: ...
    def count(self, object: _T) -> int: ...
    def insert(self, index: int, object: _T) -> None: ...
    def remove(self, object: _T) -> None: ...
    def reverse(self) -> None: ...
    def sort(self, *, key: Callable[[_T], Any] = None, reverse: bool = ...) -> None: ...

    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...
    @overload
    def __getitem__(self, i: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> List[_T]: ...
    @overload
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Sequence[_T]) -> None: ...
    def __delitem__(self, i: Union[int, slice]) -> None: ...
    def __add__(self, x: List[_T]) -> List[_T]: ...
    def __iadd__(self, x: Iterable[_T]) -> List[_T]: ...
    def __mul__(self, n: int) -> List[_T]: ...
    def __rmul__(self, n: int) -> List[_T]: ...
    def __imul__(self, n: int) -> List[_T]: ...
    def __contains__(self, o: object) -> bool: ...
    def __reversed__(self) -> Iterator[_T]: ...
    def __gt__(self, x: List[_T]) -> bool: ...
    def __ge__(self, x: List[_T]) -> bool: ...
    def __lt__(self, x: List[_T]) -> bool: ...
    def __le__(self, x: List[_T]) -> bool: ...

class dict(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
    # NOTE: Keyword arguments are special. If they are used, _KT must include
    #       str, but we have no way of enforcing it here.
    @overload
    def __init__(self, **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, map: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> Dict[_KT, _VT]: ...
    def get(self, k: _KT, default: _VT = None) -> _VT: ...
    def pop(self, k: _KT, default: _VT = None) -> _VT: ...
    def popitem(self) -> Tuple[_KT, _VT]: ...
    def setdefault(self, k: _KT, default: _VT = None) -> _VT: ...
    @overload
    def update(self, m: Mapping[_KT, _VT]) -> None: ...
    @overload
    def update(self, m: Iterable[Tuple[_KT, _VT]]) -> None: ...
    def keys(self) -> KeysView[_KT]: ...
    def values(self) -> ValuesView[_VT]: ...
    def items(self) -> ItemsView[_KT, _VT]: ...
    @staticmethod
    @overload
    def fromkeys(seq: Sequence[_T]) -> Dict[_T, Any]: ...  # TODO: Actually a class method
    @staticmethod
    @overload
    def fromkeys(seq: Sequence[_T], value: _S) -> Dict[_T, _S]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    def __delitem__(self, v: _KT) -> None: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __str__(self) -> str: ...

class set(MutableSet[_T], Generic[_T]):
    def __init__(self, iterable: Iterable[_T]=None) -> None: ...
    def add(self, element: _T) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> set[_T]: ...
    def difference(self, *s: Iterable[Any]) -> set[_T]: ...
    def difference_update(self, *s: Iterable[Any]) -> None: ...
    def discard(self, element: _T) -> None: ...
    def intersection(self, *s: Iterable[Any]) -> set[_T]: ...
    def intersection_update(self, *s: Iterable[Any]) -> None: ...
    def isdisjoint(self, s: Iterable[Any]) -> bool: ...
    def issubset(self, s: Iterable[Any]) -> bool: ...
    def issuperset(self, s: Iterable[Any]) -> bool: ...
    def pop(self) -> _T: ...
    def remove(self, element: _T) -> None: ...
    def symmetric_difference(self, s: Iterable[_T]) -> set[_T]: ...
    def symmetric_difference_update(self, s: Iterable[_T]) -> None: ...
    def union(self, *s: Iterable[_T]) -> set[_T]: ...
    def update(self, *s: Iterable[_T]) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __str__(self) -> str: ...
    def __and__(self, s: AbstractSet[Any]) -> set[_T]: ...
    def __iand__(self, s: AbstractSet[Any]) -> set[_T]: ...
    def __or__(self, s: AbstractSet[_S]) -> set[Union[_T, _S]]: ...
    def __ior__(self, s: AbstractSet[_S]) -> set[Union[_T, _S]]: ...
    def __sub__(self, s: AbstractSet[Any]) -> set[_T]: ...
    def __isub__(self, s: AbstractSet[Any]) -> set[_T]: ...
    def __xor__(self, s: AbstractSet[_S]) -> set[Union[_T, _S]]: ...
    def __ixor__(self, s: AbstractSet[_S]) -> set[Union[_T, _S]]: ...
    def __le__(self, s: AbstractSet[Any]) -> bool: ...
    def __lt__(self, s: AbstractSet[Any]) -> bool: ...
    def __ge__(self, s: AbstractSet[Any]) -> bool: ...
    def __gt__(self, s: AbstractSet[Any]) -> bool: ...
    # TODO more set operations

class frozenset(AbstractSet[_T], Generic[_T]):
    def __init__(self, iterable: Iterable[_T]=None) -> None: ...
    def copy(self) -> frozenset[_T]: ...
    def difference(self, *s: Iterable[Any]) -> frozenset[_T]: ...
    def intersection(self, *s: Iterable[Any]) -> frozenset[_T]: ...
    def isdisjoint(self, s: Iterable[_T]) -> bool: ...
    def issubset(self, s: Iterable[Any]) -> bool: ...
    def issuperset(self, s: Iterable[Any]) -> bool: ...
    def symmetric_difference(self, s: Iterable[_T]) -> frozenset[_T]: ...
    def union(self, *s: Iterable[_T]) -> frozenset[_T]: ...
    def __len__(self) -> int: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __str__(self) -> str: ...
    def __and__(self, s: AbstractSet[_T]) -> frozenset[_T]: ...
    def __or__(self, s: AbstractSet[_S]) -> frozenset[Union[_T, _S]]: ...
    def __sub__(self, s: AbstractSet[_T]) -> frozenset[_T]: ...
    def __xor__(self, s: AbstractSet[_S]) -> frozenset[Union[_T, _S]]: ...
    def __le__(self, s: AbstractSet[Any]) -> bool: ...
    def __lt__(self, s: AbstractSet[Any]) -> bool: ...
    def __ge__(self, s: AbstractSet[Any]) -> bool: ...
    def __gt__(self, s: AbstractSet[Any]) -> bool: ...

class enumerate(Iterator[Tuple[int, _T]], Generic[_T]):
    def __init__(self, iterable: Iterable[_T], start: int = 0) -> None: ...
    def __iter__(self) -> Iterator[Tuple[int, _T]]: ...
    def __next__(self) -> Tuple[int, _T]: ...
    # TODO __getattribute__

class range(Sequence[int]):
    @overload
    def __init__(self, stop: int) -> None: ...
    @overload
    def __init__(self, start: int, stop: int, step: int = 1) -> None: ...
    def count(self, value: int) -> int: ...
    def index(self, value: int, start: int = 0, stop: int = None) -> int: ...
    def __len__(self) -> int: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[int]: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> range: ...
    def __repr__(self) -> str: ...
    def __reversed__(self) -> Iterator[int]: ...

class module:
    # TODO not defined in builtins!
    __name__ = ...  # type: str
    __file__ = ...  # type: str
    __dict__ = ...  # type: Dict[str, Any]

class property:
    def __init__(self, fget: Callable[[Any], Any] = None,
                 fset: Callable[[Any, Any], None] = None,
                 fdel: Callable[[Any], None] = None, doc: str = None) -> None: ...
    def getter(self, fget: Callable[[Any], Any]) -> property: ...
    def setter(self, fset: Callable[[Any, Any], None]) -> property: ...
    def deleter(self, fdel: Callable[[Any], None]) -> property: ...
    def __get__(self, obj: Any, type: type=None) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...
    def __delete__(self, obj: Any) -> None: ...

NotImplemented = ...  # type: Any

def abs(n: SupportsAbs[_T]) -> _T: ...
def all(i: Iterable) -> bool: ...
def any(i: Iterable) -> bool: ...
def ascii(o: object) -> str: ...
def bin(number: int) -> str: ...
def callable(o: object) -> bool: ...
def chr(code: int) -> str: ...
def compile(source: Any, filename: Union[str, bytes], mode: str, flags: int = 0,
            dont_inherit: int = 0) -> Any: ...
def copyright() -> None: ...
def credits() -> None: ...
def delattr(o: Any, name: str) -> None: ...
def dir(o: object = None) -> List[str]: ...
_N = TypeVar('_N', int, float)
def divmod(a: _N, b: _N) -> Tuple[_N, _N]: ...
def eval(source: str, globals: Dict[str, Any] = None,
         locals: Mapping[str, Any] = None) -> Any: ...  # TODO code object as source
def exec(object: str, globals: Dict[str, Any] = None,
         locals: Mapping[str, Any] = None) -> Any: ...  # TODO code object as source
def exit(code: int = None) -> None: ...
def filter(function: Callable[[_T], Any], iterable: Iterable[_T]) -> Iterator[_T]: ...
def format(o: object, format_spec: str = '') -> str: ...
def getattr(o: Any, name: str, default: Any = None) -> Any: ...
def globals() -> Dict[str, Any]: ...
def hasattr(o: Any, name: str) -> bool: ...
def hash(o: object) -> int: ...
def help(*args: Any, **kwds: Any) -> None: ...
def hex(i: int) -> str: ...  # TODO __index__
def id(o: object) -> int: ...
def input(prompt: str = None) -> str: ...
@overload
def iter(iterable: Iterable[_T]) -> Iterator[_T]: ...
@overload
def iter(function: Callable[[], _T], sentinel: _T) -> Iterator[_T]: ...
def isinstance(o: object, t: Union[type, Tuple[type, ...]]) -> bool: ...
def issubclass(cls: type, classinfo: type) -> bool: ...
# TODO support this
#def issubclass(type cld, classinfo: Sequence[type]) -> bool: ...
def len(o: Sized) -> int: ...
def license() -> None: ...
def locals() -> Dict[str, Any]: ...
@overload
def map(func: Callable[[_T1], _S], iter1: Iterable[_T1]) -> Iterator[_S]: ...
@overload
def map(func: Callable[[_T1, _T2], _S], iter1: Iterable[_T1],
        iter2: Iterable[_T2]) -> Iterator[_S]: ...  # TODO more than two iterables
@overload
def max(arg1: _T, arg2: _T, *args: _T, key: Callable[[_T], Any] = None) -> _T: ...
@overload
def max(iterable: Iterable[_T], key: Callable[[_T], Any] = None, default:_T = None) -> _T: ...
# TODO memoryview
@overload
def min(arg1: _T, arg2: _T, *args: _T, key: Callable[[_T], Any] = None) -> _T: ...
@overload
def min(iterable: Iterable[_T], key: Callable[[_T], Any] = None, default:_T = None) -> _T: ...
@overload
def next(i: Iterator[_T]) -> _T: ...
@overload
def next(i: Iterator[_T], default: _T) -> _T: ...
def oct(i: int) -> str: ...  # TODO __index__
def open(file: Union[str, bytes, int], mode: str = 'r', buffering: int = -1, encoding: str = None,
         errors: str = None, newline: str = None, closefd: bool = ...) -> IO[Any]: ...
def ord(c: Union[str, bytes, bytearray]) -> int: ...
# TODO: in Python 3.2, print() does not support flush
def print(*values: Any, sep: str = ' ', end: str = '\n', file: IO[str] = None, flush: bool = False) -> None: ...
@overload
def pow(x: int, y: int) -> Any: ...  # The return type can be int or float, depending on y
@overload
def pow(x: int, y: int, z: int) -> Any: ...
@overload
def pow(x: float, y: float) -> float: ...
@overload
def pow(x: float, y: float, z: float) -> float: ...
def quit(code: int = None) -> None: ...
@overload
def reversed(object: Reversible[_T]) -> Iterator[_T]: ...
@overload
def reversed(object: Sequence[_T]) -> Iterator[_T]: ...
def repr(o: object) -> str: ...
@overload
def round(number: float) -> int: ...
@overload
def round(number: float, ndigits: int) -> float: ...  # Always return a float if given ndigits.
@overload
def round(number: SupportsRound[_T]) -> _T: ...
@overload
def round(number: SupportsRound[_T], ndigits: int) -> _T: ...
def setattr(object: Any, name: str, value: Any) -> None: ...
def sorted(iterable: Iterable[_T], *, key: Callable[[_T], Any] = None,
           reverse: bool = False) -> List[_T]: ...
def sum(iterable: Iterable[_T], start: _T = None) -> _T: ...
def vars(object: Any = None) -> Dict[str, Any]: ...
@overload
def zip(iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def zip(iter1: Iterable[_T1], iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def zip(iter1: Iterable[_T1], iter2: Iterable[_T2],
        iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def zip(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3],
        iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2,
                                               _T3, _T4]]: ... # TODO more than four iterables
def __import__(name: str, globals: Dict[str, Any] = {}, locals: Dict[str, Any] = {},
               fromlist: List[str] = [], level: int = -1) -> Any: ...

# Ellipsis

# Actually the type of Ellipsis is <type 'ellipsis'>, but since it's
# not exposed anywhere under that name, we make it private here.
class ellipsis: ...
Ellipsis = ...  # type: ellipsis

# Exceptions

class BaseException:
    args = ...  # type: Any
    __cause__ = ... # type: BaseException
    __context__ = ... # type: BaseException
    __traceback__ = ... # type: TracebackType
    def __init__(self, *args: Any) -> None: ...
    def with_traceback(self, tb: Any) -> BaseException: ...

class GeneratorExit(BaseException): ...
class KeyboardInterrupt(BaseException): ...
class SystemExit(BaseException):
    code = 0
class Exception(BaseException): ...
class ArithmeticError(Exception): ...
class EnvironmentError(Exception):
    errno = 0
    strerror = ...  # type: str
    # TODO can this be bytes?
    filename = ...  # type: str
class LookupError(Exception): ...
class RuntimeError(Exception): ...
class ValueError(Exception): ...
class AssertionError(Exception): ...
class AttributeError(Exception): ...
class BufferError(Exception): ...
class EOFError(Exception): ...
class FloatingPointError(ArithmeticError): ...
class IOError(EnvironmentError): ...
class ImportError(Exception): ...
class IndexError(LookupError): ...
class KeyError(LookupError): ...
class MemoryError(Exception): ...
class NameError(Exception): ...
class NotImplementedError(RuntimeError): ...
class OSError(EnvironmentError): ...
class BlockingIOError(OSError):
    characters_written = 0
class ChildProcessError(OSError): ...
class ConnectionError(OSError): ...
class BrokenPipeError(ConnectionError): ...
class ConnectionAbortedError(ConnectionError): ...
class ConnectionRefusedError(ConnectionError): ...
class ConnectionResetError(ConnectionError): ...
class FileExistsError(OSError): ...
class FileNotFoundError(OSError): ...
class InterruptedError(OSError): ...
class IsADirectoryError(OSError): ...
class NotADirectoryError(OSError): ...
class PermissionError(OSError): ...
class ProcessLookupError(OSError): ...
class TimeoutError(OSError): ...
class WindowsError(OSError): ...
class OverflowError(ArithmeticError): ...
class ReferenceError(Exception): ...
class StopIteration(Exception):
    value = ...  # type: Any
if sys.version_info >= (3, 5):
    class StopAsyncIteration(Exception):
        value = ...  # type: Any
class SyntaxError(Exception):
    msg = ...  # type: str
    lineno = ...  # type: int
    offset = ...  # type: int
    text = ...  # type: str
class IndentationError(SyntaxError): ...
class TabError(IndentationError): ...
class SystemError(Exception): ...
class TypeError(Exception): ...
class UnboundLocalError(NameError): ...
class UnicodeError(ValueError): ...
class UnicodeDecodeError(UnicodeError):
    encoding = ... # type: str
    object = ... # type: bytes
    start = ... # type: int
    end = ... # type: int
    reason = ... # type: str
    def __init__(self, __encoding: str, __object: bytes, __start: int, __end: int,
                 __reason: str) -> None: ...
class UnicodeEncodeError(UnicodeError): ...
class UnicodeTranslateError(UnicodeError): ...
class ZeroDivisionError(ArithmeticError): ...

class Warning(Exception): ...
class UserWarning(Warning): ...
class DeprecationWarning(Warning): ...
class SyntaxWarning(Warning): ...
class RuntimeWarning(Warning): ...
class FutureWarning(Warning): ...
class PendingDeprecationWarning(Warning): ...
class ImportWarning(Warning): ...
class UnicodeWarning(Warning): ...
class BytesWarning(Warning): ...
class ResourceWarning(Warning): ...
