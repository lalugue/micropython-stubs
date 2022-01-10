from typing import Any

class Pbhub:
    def _available() -> None: ...
    def analogRead() -> None: ...
    def deinit() -> None: ...
    def digitalRead() -> None: ...
    def digitalWrite() -> None: ...
    def setBrightness() -> None: ...
    def setColor() -> None: ...
    def setColorPos() -> None: ...
    def setRgbNum() -> None: ...

hub_addr: Any
i2c_bus: Any
unit: Any