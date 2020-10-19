
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class EventLoop:
    def call_at_() -> None: ...
    def call_later() -> None: ...
    def call_later_ms() -> None: ...
    def call_soon() -> None: ...
    def close() -> None: ...
    def create_task() -> None: ...
    def run_forever() -> None: ...
    def run_until_complete() -> None: ...
    def stop() -> None: ...
    def time() -> None: ...
    def wait() -> None: ...
class IORead: ...
class IOReadDone: ...
class IOWrite: ...
class IOWriteDone: ...
class PollEventLoop:
    def add_reader() -> None: ...
    def add_writer() -> None: ...
    def remove_reader() -> None: ...
    def remove_writer() -> None: ...
    def wait() -> None: ...
class SleepMs: ...
class StopLoop: ...
class StreamReader: ...
class StreamWriter:
    def get_extra_info() -> None: ...
class SysCall:
    def handle() -> None: ...
class SysCall1: ...
def Task() -> None: ...
def coroutine() -> None: ...
def ensure_future() -> None: ...
def get_event_loop() -> None: ...
def set_debug() -> None: ...
class type_gen:
    def close() -> None: ...
    def send() -> None: ...
    def throw() -> None: ...