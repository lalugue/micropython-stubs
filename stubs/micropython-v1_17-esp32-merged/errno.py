"""
system error codes. See: https://docs.micropython.org/en/v1.17/library/errno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""
# MCU: {'ver': 'v1.17', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4

EACCES = 13  # type: int
EADDRINUSE = 112  # type: int
EAGAIN = 11  # type: int
EALREADY = 120  # type: int
EBADF = 9  # type: int
ECONNABORTED = 113  # type: int
ECONNREFUSED = 111  # type: int
ECONNRESET = 104  # type: int
EEXIST = 17  # type: int
EHOSTUNREACH = 118  # type: int
EINPROGRESS = 119  # type: int
EINVAL = 22  # type: int
EIO = 5  # type: int
EISDIR = 21  # type: int
ENOBUFS = 105  # type: int
ENODEV = 19  # type: int
ENOENT = 2  # type: int
ENOMEM = 12  # type: int
ENOTCONN = 128  # type: int
EOPNOTSUPP = 95  # type: int
EPERM = 1  # type: int
ETIMEDOUT = 116  # type: int
errorcode = {}  # type: dict
