from typing import Any

def open(*args, **kwargs) -> Any: ...

class BytesIO:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def readline(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def flush(self, *args, **kwargs) -> Any: ...
    def getvalue(self, *args, **kwargs) -> Any: ...
    def seek(self, *args, **kwargs) -> Any: ...

class FileIO:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def readline(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def flush(self, *args, **kwargs) -> Any: ...
    def readlines(self, *args, **kwargs) -> Any: ...
    def seek(self, *args, **kwargs) -> Any: ...
    def tell(self, *args, **kwargs) -> Any: ...

class IOBase:
    def __init__(self, *argv, **kwargs) -> None: ...

class StringIO:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def readline(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def flush(self, *args, **kwargs) -> Any: ...
    def getvalue(self, *args, **kwargs) -> Any: ...
    def seek(self, *args, **kwargs) -> Any: ...

class TextIOWrapper:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def readline(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def flush(self, *args, **kwargs) -> Any: ...
    def readlines(self, *args, **kwargs) -> Any: ...
    def seek(self, *args, **kwargs) -> Any: ...
    def tell(self, *args, **kwargs) -> Any: ...
