# Micropython 1.19.1 frozen stubs
from _typeshed import Incomplete
from ubinascii import hexlify as hexlify

class MQTTException(Exception): ...

class MQTTClient:
    client_id: Incomplete
    sock: Incomplete
    server: Incomplete
    port: Incomplete
    ssl: Incomplete
    ssl_params: Incomplete
    pid: int
    cb: Incomplete
    user: Incomplete
    pswd: Incomplete
    keepalive: Incomplete
    lw_topic: Incomplete
    lw_msg: Incomplete
    lw_qos: int
    lw_retain: bool
    def __init__(
        self,
        client_id,
        server,
        port: int = ...,
        user: Incomplete | None = ...,
        password: Incomplete | None = ...,
        keepalive: int = ...,
        ssl: bool = ...,
        ssl_params=...,
    ) -> None: ...
    def _send_str(self, s) -> None: ...
    def _recv_len(self): ...
    def set_callback(self, f) -> None: ...
    def set_last_will(self, topic, msg, retain: bool = ..., qos: int = ...) -> None: ...
    def connect(self, clean_session: bool = ...): ...
    def disconnect(self) -> None: ...
    def ping(self) -> None: ...
    def publish(self, topic, msg, retain: bool = ..., qos: int = ...) -> None: ...
    def subscribe(self, topic, qos: int = ...) -> None: ...
    def wait_msg(self): ...
    def check_msg(self): ...
