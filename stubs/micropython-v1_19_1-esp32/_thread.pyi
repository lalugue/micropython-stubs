from typing import Any

def get_ident(*args, **kwargs) -> Any: ...
def start_new_thread(*args, **kwargs) -> Any: ...
def stack_size(*args, **kwargs) -> Any: ...
def exit(*args, **kwargs) -> Any: ...
def allocate_lock(*args, **kwargs) -> Any: ...

class LockType:
    def locked(self, *args, **kwargs) -> Any: ...
    def release(self, *args, **kwargs) -> Any: ...
    def acquire(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...