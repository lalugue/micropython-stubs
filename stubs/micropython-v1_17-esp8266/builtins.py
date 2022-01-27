"""
Module: 'builtins' on micropython-v1.17-esp8266
"""
# MCU: {'ver': 'v1.17', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.17', 'name': 'micropython', 'mpy': 9733, 'version': '1.17', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any


class ArithmeticError(Exception):
    """"""


class AssertionError(Exception):
    """"""


class AttributeError(Exception):
    """"""


class EOFError(Exception):
    """"""


Ellipsis: Any  ## <class ''> = Ellipsis


class GeneratorExit:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class ImportError(Exception):
    """"""


class IndentationError(Exception):
    """"""


class IndexError(Exception):
    """"""


class KeyError(Exception):
    """"""


class KeyboardInterrupt:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class LookupError(Exception):
    """"""


class MemoryError(Exception):
    """"""


class NameError(Exception):
    """"""


class NotImplementedError(Exception):
    """"""


class OSError(Exception):
    """"""


class OverflowError(Exception):
    """"""


class RuntimeError(Exception):
    """"""


class StopIteration:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class SyntaxError(Exception):
    """"""


class SystemExit:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class TypeError(Exception):
    """"""


class ValueError(Exception):
    """"""


class ZeroDivisionError(Exception):
    """"""


def abs(*args) -> Any:
    ...


def all(*args) -> Any:
    ...


def any(*args) -> Any:
    ...


class bool:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class bytearray:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def append(self, *args) -> Any:
        ...

    def extend(self, *args) -> Any:
        ...

    def decode(self, *args) -> Any:
        ...


class bytes:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def count(self, *args) -> Any:
        ...

    def endswith(self, *args) -> Any:
        ...

    def find(self, *args) -> Any:
        ...

    def format(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...

    def isalpha(self, *args) -> Any:
        ...

    def isdigit(self, *args) -> Any:
        ...

    def islower(self, *args) -> Any:
        ...

    def isspace(self, *args) -> Any:
        ...

    def isupper(self, *args) -> Any:
        ...

    def join(self, *args) -> Any:
        ...

    def lower(self, *args) -> Any:
        ...

    def lstrip(self, *args) -> Any:
        ...

    def replace(self, *args) -> Any:
        ...

    def rfind(self, *args) -> Any:
        ...

    def rindex(self, *args) -> Any:
        ...

    def rsplit(self, *args) -> Any:
        ...

    def rstrip(self, *args) -> Any:
        ...

    def split(self, *args) -> Any:
        ...

    def startswith(self, *args) -> Any:
        ...

    def strip(self, *args) -> Any:
        ...

    def upper(self, *args) -> Any:
        ...

    def decode(self, *args) -> Any:
        ...


def callable(*args) -> Any:
    ...


def chr(*args) -> Any:
    ...


class dict:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def clear(self, *args) -> Any:
        ...

    def copy(self, *args) -> Any:
        ...

    def get(self, *args) -> Any:
        ...

    def items(self, *args) -> Any:
        ...

    def keys(self, *args) -> Any:
        ...

    def pop(self, *args) -> Any:
        ...

    def popitem(self, *args) -> Any:
        ...

    def setdefault(self, *args) -> Any:
        ...

    def update(self, *args) -> Any:
        ...

    def values(self, *args) -> Any:
        ...

    @classmethod
    def fromkeys(cls, *args) -> Any:
        ...


def dir(*args) -> Any:
    ...


def divmod(*args) -> Any:
    ...


def eval(*args) -> Any:
    ...


def exec(*args) -> Any:
    ...


def getattr(*args) -> Any:
    ...


def globals(*args) -> Any:
    ...


def hasattr(*args) -> Any:
    ...


def hash(*args) -> Any:
    ...


def id(*args) -> Any:
    ...


class int:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    @classmethod
    def from_bytes(cls, *args) -> Any:
        ...

    def to_bytes(self, *args) -> Any:
        ...


def isinstance(*args) -> Any:
    ...


def issubclass(*args) -> Any:
    ...


def iter(*args) -> Any:
    ...


def len(*args) -> Any:
    ...


class list:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def append(self, *args) -> Any:
        ...

    def clear(self, *args) -> Any:
        ...

    def copy(self, *args) -> Any:
        ...

    def count(self, *args) -> Any:
        ...

    def extend(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...

    def insert(self, *args) -> Any:
        ...

    def pop(self, *args) -> Any:
        ...

    def remove(self, *args) -> Any:
        ...

    def reverse(self, *args) -> Any:
        ...

    def sort(self, *args) -> Any:
        ...


def locals(*args) -> Any:
    ...


class map:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def next(*args) -> Any:
    ...


class object:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def __init__(self, *args) -> None:
        ...


def open(*args) -> Any:
    ...


def ord(*args) -> Any:
    ...


def pow(*args) -> Any:
    ...


def print(*args) -> Any:
    ...


class range:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def repr(*args) -> Any:
    ...


def round(*args) -> Any:
    ...


class set:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def clear(self, *args) -> Any:
        ...

    def copy(self, *args) -> Any:
        ...

    def pop(self, *args) -> Any:
        ...

    def remove(self, *args) -> Any:
        ...

    def update(self, *args) -> Any:
        ...

    def add(self, *args) -> Any:
        ...

    def difference(self, *args) -> Any:
        ...

    def difference_update(self, *args) -> Any:
        ...

    def discard(self, *args) -> Any:
        ...

    def intersection(self, *args) -> Any:
        ...

    def intersection_update(self, *args) -> Any:
        ...

    def isdisjoint(self, *args) -> Any:
        ...

    def issubset(self, *args) -> Any:
        ...

    def issuperset(self, *args) -> Any:
        ...

    def symmetric_difference(self, *args) -> Any:
        ...

    def symmetric_difference_update(self, *args) -> Any:
        ...

    def union(self, *args) -> Any:
        ...


def setattr(*args) -> Any:
    ...


def sorted(*args) -> Any:
    ...


class str:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def count(self, *args) -> Any:
        ...

    def endswith(self, *args) -> Any:
        ...

    def find(self, *args) -> Any:
        ...

    def format(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...

    def isalpha(self, *args) -> Any:
        ...

    def isdigit(self, *args) -> Any:
        ...

    def islower(self, *args) -> Any:
        ...

    def isspace(self, *args) -> Any:
        ...

    def isupper(self, *args) -> Any:
        ...

    def join(self, *args) -> Any:
        ...

    def lower(self, *args) -> Any:
        ...

    def lstrip(self, *args) -> Any:
        ...

    def replace(self, *args) -> Any:
        ...

    def rfind(self, *args) -> Any:
        ...

    def rindex(self, *args) -> Any:
        ...

    def rsplit(self, *args) -> Any:
        ...

    def rstrip(self, *args) -> Any:
        ...

    def split(self, *args) -> Any:
        ...

    def startswith(self, *args) -> Any:
        ...

    def strip(self, *args) -> Any:
        ...

    def upper(self, *args) -> Any:
        ...

    def encode(self, *args) -> Any:
        ...


def sum(*args) -> Any:
    ...


class super:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class tuple:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def count(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...


class type:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class zip:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class StopAsyncIteration:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class UnicodeError(Exception):
    """"""


class ViperTypeError(Exception):
    """"""


def bin(*args) -> Any:
    ...


def delattr(*args) -> Any:
    ...


class enumerate:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class filter:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class float:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class frozenset:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def copy(self, *args) -> Any:
        ...

    def difference(self, *args) -> Any:
        ...

    def intersection(self, *args) -> Any:
        ...

    def isdisjoint(self, *args) -> Any:
        ...

    def issubset(self, *args) -> Any:
        ...

    def issuperset(self, *args) -> Any:
        ...

    def symmetric_difference(self, *args) -> Any:
        ...

    def union(self, *args) -> Any:
        ...


def help(*args) -> Any:
    ...


def hex(*args) -> Any:
    ...


def input(*args) -> Any:
    ...


def max(*args) -> Any:
    ...


class memoryview:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def min(*args) -> Any:
    ...


def oct(*args) -> Any:
    ...


class property:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def deleter(self, *args) -> Any:
        ...

    def getter(self, *args) -> Any:
        ...

    def setter(self, *args) -> Any:
        ...


class reversed:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class slice:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...
