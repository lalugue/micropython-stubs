class DriveBase:
    def drive() -> None: ...
    def drive_time() -> None: ...
    def stop() -> None: ...

class Stop:
    BRAKE: int
    COAST: int
    HOLD: int

pi: float

def wait() -> None: ...