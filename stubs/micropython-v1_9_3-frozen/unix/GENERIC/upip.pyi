from _typeshed import Incomplete

debug: bool
install_path: Incomplete
cleanup_files: Incomplete
gzdict_sz: Incomplete
file_buf: Incomplete

class NotFoundError(Exception): ...

def op_split(path): ...
def op_basename(path): ...
def _makedirs(name, mode: int = ...): ...
def save_file(fname, subf) -> None: ...
def install_tar(f, prefix): ...
def expandhome(s): ...

warn_ussl: bool

def url_open(url): ...
def get_pkg_metadata(name): ...
def fatal(msg, exc: Incomplete | None = ...) -> None: ...
def install_pkg(pkg_spec, install_path): ...
def install(to_install, install_path: Incomplete | None = ...) -> None: ...
def get_install_path(): ...
def cleanup() -> None: ...
def help() -> None: ...
def main() -> None: ...
