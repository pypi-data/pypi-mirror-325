#!/usr/bin/env python

from typing import Any, Callable, Optional, TextIO, Union

from .ansi import (  # noqa
    BLACK,
    BLACK_BG,
    BLUE,
    BLUE_BG,
    BOLD,
    CYAN,
    CYAN_BG,
    ERASE_LINE,
    GREEN,
    GREEN_BG,
    NEGATIVE,
    NL,
    PURPLE,
    PURPLE_BG,
    RED,
    RED_BG,
    RESET,
    SPACE,
    WHITE,
    WHITE_BG,
    YELLOW,
    YELLOW_BG,
)
from .info import InfoStyle, get_style

__all__ = ["Config"]


class Config:
    def __init__(
        self,
        fullscreen: bool,
        height: Optional[int],
        format_fn: Callable[[Any], str],
        info_style: Union[InfoStyle, str],
        pointer_str: str,
        prompt_str: str,
        header_str: str,
        lazy: bool,
        output_stream: TextIO,
        auto_refresh: Optional[int],
    ):
        """
        Finder config

        Args:
            fullscreen: Full screen mode
            height: Finder window height
            format_fn: Items format function
            info_style: Determines the display style of finder info
            pointer_str: Pointer to the current line
            prompt_str: Input prompt
            header_str: Header
            lazy: Lazy mode, starts the finder only if the candidates are more than one
            output_stream: Output stream
            auto_refresh: Auto refresh period (in seconds)
        """
        self.fullscreen = fullscreen
        self.height = height
        self.format_fn = format_fn
        self.info_style: InfoStyle = get_style(info_style)
        self.pointer_str = pointer_str
        self.no_pointer_str = " " * len(pointer_str)
        self.prompt_str = prompt_str
        self.header_str = header_str
        self.lazy = lazy
        self.output_stream = output_stream
        self.auto_refresh = auto_refresh

    @property
    def info_lines(self) -> int:
        "Number of info lines"
        return 1 if self.info_style == InfoStyle.DEFAULT else 0

    @property
    def prompt_lines(self) -> int:
        "Number of prompt lines"
        return len(self.prompt_str.split(f"{NL}"))

    @property
    def header_lines(self) -> int:
        "Number of header lines"
        return len(self.header_str.split(f"{NL}")) if self.header_str else 0

    @property
    def margin_lines(self) -> int:
        "Screen margin"
        return self.info_lines + self.prompt_lines + self.header_lines
