from typing import Any

class Event:
    def clear() -> None: ...
    def is_set() -> None: ...
    def set() -> None: ...
    wait: Any

core: Any