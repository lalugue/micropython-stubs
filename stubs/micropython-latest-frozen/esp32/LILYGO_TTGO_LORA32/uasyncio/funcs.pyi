from . import core as core
from collections.abc import Generator
from typing import Any

async def wait_for(aw, timeout, sleep=...): ...
def wait_for_ms(aw, timeout): ...

class _Remove:
    @staticmethod
    def remove(t) -> None: ...

async def gather(*aws, return_exceptions: bool = ...) -> Generator[None, None, Any]: ...