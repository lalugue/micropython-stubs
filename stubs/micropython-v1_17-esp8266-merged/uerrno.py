"""
system error codes. See: https://docs.micropython.org/en/v1.17/library/errno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""
# MCU: {'ver': 'v1.17', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.17', 'name': 'micropython', 'mpy': 9733, 'version': '1.17', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.4

EACCES = 13  # type: int
EADDRINUSE = 98  # type: int
EAGAIN = 11  # type: int
EALREADY = 114  # type: int
EBADF = 9  # type: int
ECONNABORTED = 103  # type: int
ECONNREFUSED = 111  # type: int
ECONNRESET = 104  # type: int
EEXIST = 17  # type: int
EHOSTUNREACH = 113  # type: int
EINPROGRESS = 115  # type: int
EINVAL = 22  # type: int
EIO = 5  # type: int
EISDIR = 21  # type: int
ENOBUFS = 105  # type: int
ENODEV = 19  # type: int
ENOENT = 2  # type: int
ENOMEM = 12  # type: int
ENOTCONN = 107  # type: int
EOPNOTSUPP = 95  # type: int
EPERM = 1  # type: int
ETIMEDOUT = 110  # type: int
errorcode = {}  # type: dict
