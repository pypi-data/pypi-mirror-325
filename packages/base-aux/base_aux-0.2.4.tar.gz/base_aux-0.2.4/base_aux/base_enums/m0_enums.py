from enum import Enum, auto


# =====================================================================================================================
"""
USAGE
-----
if WHEN == When2.BEFORE:
    pass
    

print(FPoint.COMMA)     # FPoint.COMMA
print(FPoint("."))      # FPoint.DOT

print("." in FPoint)            # True
print(FPoint.DOT in FPoint)     # True

print(FPoint(".") == ".")      # False
print(FPoint(FPoint.DOT))      # FPoint.DOT     # BEST WAY to init value!


MAKE A DEFAULT NONE VALUE
-------------------------
class FPoint(Enum):
    DOT = "."
    COMMA = ","
    AUTO = None     # def! when FPoint(None)
"""


# =====================================================================================================================
class When2(Enum):
    BEFORE = auto()
    AFTER = auto()


class When3(Enum):
    BEFORE = auto()
    AFTER = auto()
    MIDDLE = auto()


# ---------------------------------------------------------------------------------------------------------------------
class Where2(Enum):
    FIRST = auto()
    LAST = auto()


class Where3(Enum):
    FIRST = auto()
    LAST = auto()
    MIDDLE = auto()


# =====================================================================================================================
class CallablesUse(Enum):
    DIRECT = auto()
    EXX = auto()
    RAISE = auto()
    RAISE_AS_NONE = auto()
    BOOL = auto()

    SKIP_CALLABLE = auto()
    SKIP_RAISED = auto()


# =====================================================================================================================
class Process(Enum):
    """
    GOAL
    ----
    define special values for methods

    SPECIALLY CREATED FOR
    ---------------------
    CallableAux.resolve when returns SKIPPED like object!
    """
    NONE = auto()
    STARTED = auto()
    SKIPPED = auto()
    STOPPED = auto()
    RAISED = auto()
    FAILED = auto()
    SUCCESS = auto()


# =====================================================================================================================
class FormIntExt(Enum):
    """
    SPECIALLY CREATED FOR
    ---------------------
    AttrAux show internal external names for PRIVATES
    """
    INTERNAL = auto()
    EXTERNAL = auto()


# =====================================================================================================================
class BoolCumulate(Enum):
    """
    GOAL
    ----
    combine result for collection

    SPECIALLY CREATED FOR
    ---------------------
    EqValid_RegexpAllTrue
    """
    ALL_TRUE = auto()
    ANY_TRUE = auto()
    ANY_FALSE = auto()
    ALL_FALSE = auto()


# =====================================================================================================================
class PathType(Enum):
    FILE = auto()
    DIR = auto()
    ALL = auto()


# ---------------------------------------------------------------------------------------------------------------------
class NumType(Enum):
    INT = auto()
    FLOAT = auto()
    BOTH = auto()


# =====================================================================================================================
class FPoint(Enum):
    """
    SPECIALLY CREATED FOR
    ---------------------
    TextAux.parse__single_number
    """
    DOT = "."
    COMMA = ","
    AUTO = None     # auto is more important for SingleNum!


TYPE__FPOINT_DRAFT = FPoint | str | None


# =====================================================================================================================
class CmpType(Enum):
    """
    SPECIALLY CREATED FOR
    ---------------------
    path1_dirs.Dir.iter(timestamp)
    """
    LT = auto()
    LE = auto()
    GT = auto()
    GE = auto()


# =====================================================================================================================
# class Represent(Enum):
#     NAME = auto()
#     OBJECT = auto()


# =====================================================================================================================
