from tkinter import *
from collections.abc import MutableSequence

import sys

class WinOCatException(Exception):
    pass

class SystemConfig:
    def __init__(self):
        self._platform = sys.platform
        if self._platform.startwith("linux"):
            self._platform = "linux"
        if PIL_AVAILABLE:
            self._supported_image_types = ["GIF", "Animated GIF", "BMP", "ICO", "PNG", "JPG", "TIF"]
        else:
            self._supported_image_types = ["GIF", "PNG"]
            if self._platform == "darwin":
                self._supported_image_types = ["GIF"]
        self._tk_options = {
            "*Label.Font": "helvetica 12",
            "*Label.Foreground": "black"
        }

    @property
    def PIL_available(self):
        return PIL_AVAILABLE
    
    @property
    def supported_image_types(self):
        return self._supported_image_types

    @property
    def platform(self):
        return self._platform

    @property
    def tk_options(self):
        return self._tk_options
    

try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

class Window(BaseWindow):
    main_window = None

    def __init__(
        self,
        title : str,
        width, height,
        leyout,
        bg=None,
        visible=True
    ):
        if Window.main_window is None:
            tk = Tk()
            Window.main_window = self
            for option_key in system_config.tk_options: