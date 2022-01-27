from typing import Any

class OneWireError(Exception): ...

class OneWire:
    def __init__(self, *argv, **kwargs) -> None: ...
    def __init__(self, *args) -> None: ...
    def readinto(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def crc8(self, *args) -> Any: ...
    def readbit(self, *args) -> Any: ...
    def readbyte(self, *args) -> Any: ...
    def reset(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def writebit(self, *args) -> Any: ...
    def writebyte(self, *args) -> Any: ...
    SEARCH_ROM: int
    MATCH_ROM: int
    SKIP_ROM: int
    def select_rom(self, *args) -> Any: ...
