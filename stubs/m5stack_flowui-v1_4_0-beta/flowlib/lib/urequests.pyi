from typing import Any

class Response:
    def close() -> None: ...
    content: Any
    def json() -> None: ...
    text: Any

def delete() -> None: ...
def get() -> None: ...
def head() -> None: ...
def patch() -> None: ...
def post() -> None: ...
def put() -> None: ...
def request() -> None: ...

usocket: Any