"""
Module: 'network' on micropython-v1.14-esp32
"""
# MCU: {'ver': 'v1.14', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.14.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.14.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any

AP_IF = 1  # type: int
AUTH_MAX = 8  # type: int
AUTH_OPEN = 0  # type: int
AUTH_WEP = 1  # type: int
AUTH_WPA2_ENTERPRISE = 5  # type: int
AUTH_WPA2_PSK = 3  # type: int
AUTH_WPA_PSK = 2  # type: int
AUTH_WPA_WPA2_PSK = 4  # type: int
MODE_11B = 1  # type: int
MODE_11G = 2  # type: int
MODE_11N = 4  # type: int
PHY_IP101 = 2  # type: int
PHY_LAN8720 = 0  # type: int
PHY_TLK110 = 1  # type: int


def PPP(*args, **kwargs) -> Any:
    ...


STAT_ASSOC_FAIL = 203  # type: int
STAT_BEACON_TIMEOUT = 200  # type: int
STAT_CONNECTING = 1001  # type: int
STAT_GOT_IP = 1010  # type: int
STAT_HANDSHAKE_TIMEOUT = 204  # type: int
STAT_IDLE = 1000  # type: int
STAT_NO_AP_FOUND = 201  # type: int
STAT_WRONG_PASSWORD = 202  # type: int
STA_IF = 0  # type: int


def WLAN(*args, **kwargs) -> Any:
    ...


def phy_mode(*args, **kwargs) -> Any:
    ...
