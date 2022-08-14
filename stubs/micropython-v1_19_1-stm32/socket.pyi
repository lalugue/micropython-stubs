from typing import Any

AF_INET: int
AF_INET6: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_STREAM: int
SOL_SOCKET: int
SO_KEEPALIVE: int
SO_RCVTIMEO: int
SO_REUSEADDR: int
SO_SNDTIMEO: int

def getaddrinfo(*args, **kwargs) -> Any: ...

class socket:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def readline(self, *args, **kwargs) -> Any: ...
    def send(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def accept(self, *args, **kwargs) -> Any: ...
    def bind(self, *args, **kwargs) -> Any: ...
    def connect(self, *args, **kwargs) -> Any: ...
    def listen(self, *args, **kwargs) -> Any: ...
    def makefile(self, *args, **kwargs) -> Any: ...
    def recv(self, *args, **kwargs) -> Any: ...
    def recvfrom(self, *args, **kwargs) -> Any: ...
    def sendall(self, *args, **kwargs) -> Any: ...
    def sendto(self, *args, **kwargs) -> Any: ...
    def setblocking(self, *args, **kwargs) -> Any: ...
    def setsockopt(self, *args, **kwargs) -> Any: ...
    def settimeout(self, *args, **kwargs) -> Any: ...