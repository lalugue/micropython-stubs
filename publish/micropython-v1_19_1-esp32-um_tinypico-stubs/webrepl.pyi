# Micropython 1.19.1 frozen stubs
from _typeshed import Incomplete

listen_s: Incomplete
client_s: Incomplete

def setup_conn(port, accept_handler): ...
def accept_conn(listen_sock) -> None: ...
def stop() -> None: ...
def start(port: int = ..., password: Incomplete | None = ..., accept_handler=...) -> None: ...
def start_foreground(port: int = ..., password: Incomplete | None = ...) -> None: ...
