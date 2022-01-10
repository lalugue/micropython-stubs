from typing import Any

class Button:
    BEACON: int
    CENTER: int
    DOWN: int
    LEFT: int
    LEFT_DOWN: int
    LEFT_UP: int
    RIGHT: int
    RIGHT_DOWN: int
    RIGHT_UP: int
    UP: int

class Color:
    BLACK: int
    BLUE: int
    BROWN: int
    GREEN: int
    ORANGE: int
    PURPLE: int
    RED: int
    WHITE: int
    YELLOW: int

class ColorSensor:
    def _close_files() -> None: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _value() -> None: ...
    def ambient() -> None: ...
    def color() -> None: ...
    def reflection() -> None: ...
    def rgb() -> None: ...

class Direction:
    CLOCKWISE: int
    COUNTERCLOCKWISE: int

class Ev3devSensor:
    def _close_files() -> None: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _value() -> None: ...

class Ev3devUartSensor:
    def _close_files() -> None: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _reset() -> None: ...
    def _reset_port() -> None: ...
    def _value() -> None: ...

class GyroSensor:
    def _calibrate() -> None: ...
    def _close_files() -> None: ...
    _default_mode: str
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _reset() -> None: ...
    def _reset_port() -> None: ...
    def _value() -> None: ...
    def angle() -> None: ...
    def reset_angle() -> None: ...
    def speed() -> None: ...

class InfraredSensor:
    def _close_files() -> None: ...
    _combinations: Any
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _value() -> None: ...
    def beacon() -> None: ...
    def buttons() -> None: ...
    def distance() -> None: ...

class Motor:
    def angle() -> None: ...
    def dc() -> None: ...
    def reset_angle() -> None: ...
    def run() -> None: ...
    def run_angle() -> None: ...
    def run_target() -> None: ...
    def run_time() -> None: ...
    def run_until_stalled() -> None: ...
    def set_dc_settings() -> None: ...
    def set_pid_settings() -> None: ...
    def set_run_settings() -> None: ...
    def speed() -> None: ...
    def stalled() -> None: ...
    def stop() -> None: ...
    def track_target() -> None: ...

class StopWatch:
    def pause() -> None: ...
    def reset() -> None: ...
    def resume() -> None: ...
    def time() -> None: ...

class TouchSensor:
    def _close_files() -> None: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _value() -> None: ...
    def pressed() -> None: ...

class UltrasonicSensor:
    PING_WAIT: int
    def _close_files() -> None: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _value() -> None: ...
    def distance() -> None: ...
    def presence() -> None: ...

def wait() -> None: ...