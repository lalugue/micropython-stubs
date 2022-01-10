from typing import Any

ONE_SHOT: int
PERIODIC: int

class Timer:
    ONE_SHOT: int
    PERIODIC: int
    def deinit() -> None: ...
    def init() -> None: ...
    def setCallback() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def update() -> None: ...

machine: Any
time: Any

class timeSch:
    ONE_SHOT: int
    PERIODIC: int
    def checkInit() -> None: ...
    def deinit() -> None: ...
    def event() -> None: ...
    def remove_all() -> None: ...
    def run() -> None: ...
    def setTimer() -> None: ...
    def stop() -> None: ...
    def timerCb() -> None: ...