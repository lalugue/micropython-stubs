from typing import Any

class _hash:
    _: Any
    def __init__(self, data: Union[Any, None] = ...) -> None: ...
    def update(self, data) -> None: ...
    def digest(self) -> None: ...

class md5(_hash): ...
class sha1(_hash): ...
class sha256(_hash): ...