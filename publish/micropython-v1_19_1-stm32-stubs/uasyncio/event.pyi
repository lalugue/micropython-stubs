# Micropython 1.19.1 frozen stubs
import uio
from . import core as core
from _typeshed import Incomplete
from collections.abc import Generator

class Event:
    state: bool
    waiting: Incomplete
    def __init__(self) -> None: ...
    def is_set(self): ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    async def wait(self) -> Generator[None, None, Incomplete]: ...

class ThreadSafeFlag(uio.IOBase):
    _flag: int
    def __init__(self) -> None: ...
    def ioctl(self, req, flags): ...
    def set(self) -> None: ...
    async def wait(self) -> Generator[Incomplete, None, None]: ...
