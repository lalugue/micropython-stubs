"""
Module: 'esp' on micropython-v1.13-266-esp32
"""
# MCU: {'ver': 'v1.13-266', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.13.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.13.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '266', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any

LOG_DEBUG = 4  # type: int
LOG_ERROR = 1  # type: int
LOG_INFO = 3  # type: int
LOG_NONE = 0  # type: int
LOG_VERBOSE = 5  # type: int
LOG_WARNING = 2  # type: int


def dht_readinto(*args, **kwargs) -> Any:
    ...


def flash_erase(*args, **kwargs) -> Any:
    ...


def flash_read(*args, **kwargs) -> Any:
    ...


def flash_size(*args, **kwargs) -> Any:
    ...


def flash_user_start(*args, **kwargs) -> Any:
    ...


def flash_write(*args, **kwargs) -> Any:
    ...


def gpio_matrix_in(*args, **kwargs) -> Any:
    ...


def gpio_matrix_out(*args, **kwargs) -> Any:
    ...


def neopixel_write(*args, **kwargs) -> Any:
    ...


def osdebug(*args, **kwargs) -> Any:
    ...
