import curses
from abc import ABC, abstractmethod

from .structs import Option


class HighlightOptionBase(ABC):
    @abstractmethod
    def render(self, stdscr: curses.window, option: Option):
        pass


class DefaultHighlightOption(HighlightOptionBase):
    def render(self, stdscr: curses.window, option: Option):
        stdscr.addstr(f"{option.label}\n", curses.color_pair(1))


class YellowHighlightOption(HighlightOptionBase):
    def render(self, stdscr: curses.window, option: Option):
        # set yellow color
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.addstr(f"{option.label}\n", curses.color_pair(2))
        stdscr.chgat(-1, curses.color_pair(2))


class LeftArrowHighlightOption(HighlightOptionBase):
    def render(self, stdscr: curses.window, option: Option):
        # set yellow color
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.addstr(f"> {option.label}\n", curses.color_pair(3))
        stdscr.chgat(-1, curses.color_pair(3))
