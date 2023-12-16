"""Color highlighters."""

import curses

from navcli.structs import Option
from .base import HighlightOptionBase


class ColorHighlightOption(HighlightOptionBase):
    """Color option highlighter."""

    def render_focused(self, stdscr: curses.window, option: Option):
        # set yellow color
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.addstr(f"{option.label}\n", curses.color_pair(2))
        stdscr.chgat(-1, curses.color_pair(2))

    def render_not_focused(self, stdscr: curses.window, option: Option):
        stdscr.addstr(f"{option.label}\n")
