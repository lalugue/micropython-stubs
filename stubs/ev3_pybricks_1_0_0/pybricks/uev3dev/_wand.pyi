
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class CompositeOp: ...
class Gravity: ...
class MagickWand:
    def _raise_error() -> None: ...
    def _set_image_depth() -> None: ...
    def _set_image_format() -> None: ...
    def _set_image_gravity() -> None: ...
    def border_image() -> None: ...
    def export_image_pixels() -> None: ...
    def extent_image() -> None: ...
    def read_image() -> None: ...
    def write_image() -> None: ...
class MagickWandError: ...
class PixelError: ...
class PixelWand:
    def _raise_error() -> None: ...
    def _set_color() -> None: ...
    def color() -> None: ...
class StorageType: ...
def bytearray_at() -> None: ...
def calcsize() -> None: ...
def unpack() -> None: ...