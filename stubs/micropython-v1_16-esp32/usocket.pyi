from typing import Any

def __init__(*args) -> None: ...

AF_INET: int
AF_INET6: int
IPPROTO_IP: int
IPPROTO_TCP: int
IPPROTO_UDP: int
IP_ADD_MEMBERSHIP: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_STREAM: int
SOL_SOCKET: int
SO_REUSEADDR: int

def getaddrinfo(*args) -> Any: ...

class socket:
    def close(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def send(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def accept(self, *args) -> Any: ...
    def bind(self, *args) -> Any: ...
    def connect(self, *args) -> Any: ...
    def fileno(self, *args) -> Any: ...
    def listen(self, *args) -> Any: ...
    def makefile(self, *args) -> Any: ...
    def recv(self, *args) -> Any: ...
    def recvfrom(self, *args) -> Any: ...
    def sendall(self, *args) -> Any: ...
    def sendto(self, *args) -> Any: ...
    def setblocking(self, *args) -> Any: ...
    def setsockopt(self, *args) -> Any: ...
    def settimeout(self, *args) -> Any: ...