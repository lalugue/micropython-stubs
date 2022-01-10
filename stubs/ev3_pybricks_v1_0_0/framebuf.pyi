class FrameBuffer:
    def blit() -> None: ...
    def fill() -> None: ...
    def fill_rect() -> None: ...
    def hline() -> None: ...
    def line() -> None: ...
    def pixel() -> None: ...
    def rect() -> None: ...
    def scroll() -> None: ...
    def text() -> None: ...
    def vline() -> None: ...

def FrameBuffer1() -> None: ...

GS2_HMSB: int
GS4_HMSB: int
GS8: int
MONO_HLSB: int
MONO_HMSB: int
MONO_VLSB: int
MVLSB: int
RGB565: int
XRGB8888: int