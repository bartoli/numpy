import sys
from typing import (
    TypeVar,
    Optional,
    Type,
    Union,
    Tuple,
    Sequence,
    overload,
    Any,
    TypeVar,
    Dict,
    List,
)

from numpy import generic, ndarray, dtype

from numpy.core._type_aliases import (
    sctypeDict as sctypeDict,
    sctypes as sctypes,
)

from numpy.typing import DTypeLike, ArrayLike

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol, TypedDict
else:
    from typing_extensions import Literal, Protocol, TypedDict

_T = TypeVar("_T")
_ScalarType = TypeVar("_ScalarType", bound=generic)

class _CastFunc(Protocol):
    def __call__(
        self, x: ArrayLike, k: DTypeLike = ...
    ) -> ndarray[Any, dtype[Any]]: ...

class _TypeCodes(TypedDict):
    Character: Literal['c']
    Integer: Literal['bhilqp']
    UnsignedInteger: Literal['BHILQP']
    Float: Literal['efdg']
    Complex: Literal['FDG']
    AllInteger: Literal['bBhHiIlLqQpP']
    AllFloat: Literal['efdgFDG']
    Datetime: Literal['Mm']
    All: Literal['?bhilqpBHILQPefdgFDGSUVOMm']

class _typedict(Dict[Type[generic], _T]):
    def __getitem__(self, key: DTypeLike) -> _T: ...

__all__: List[str]

def maximum_sctype(t: DTypeLike) -> dtype: ...
def issctype(rep: object) -> bool: ...
@overload
def obj2sctype(rep: object) -> Optional[generic]: ...
@overload
def obj2sctype(rep: object, default: None) -> Optional[generic]: ...
@overload
def obj2sctype(
    rep: object, default: Type[_T]
) -> Union[generic, Type[_T]]: ...
def issubclass_(arg1: object, arg2: Union[object, Tuple[object, ...]]) -> bool: ...
def issubsctype(
    arg1: Union[ndarray, DTypeLike], arg2: Union[ndarray, DTypeLike]
) -> bool: ...
def issubdtype(arg1: DTypeLike, arg2: DTypeLike) -> bool: ...
def sctype2char(sctype: object) -> str: ...
def find_common_type(
    array_types: Sequence[DTypeLike], scalar_types: Sequence[DTypeLike]
) -> dtype: ...

cast: _typedict[_CastFunc]
nbytes: _typedict[int]
typecodes: _TypeCodes
ScalarType: Tuple[type, ...]
