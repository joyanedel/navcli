"""Highlighters for arrow options."""

import curses

from typing import NamedTuple

from navcli.structs import Option
from .base import HighlightOptionBase

OuterIndicator = NamedTuple("outer_indicator", [("left", str), ("right", str)])


class LeftIndicatorHighlightOption(HighlightOptionBase):
    """Indicator option highlighter.

    This highlighter adds an indicator to the focused option.

    Example:

    ::

      > Option 1
        Option 2
        Option 3
        ------------------
        Option 1
      > Option 2
        Option 3
        ------------------
        Option 1
        Option 2
      > Option 3

    """

    def __init__(self, indicator: str = ">") -> None:
        self.indicator = indicator
        self.indicator_length = len(indicator)

    def render_focused(self, stdscr: curses.window, option: Option):
        # set yellow color
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.addstr(f"{self.indicator} {option.label}\n", curses.color_pair(3))
        stdscr.chgat(-1, curses.color_pair(3))

    def render_not_focused(self, stdscr: curses.window, option: Option):
        stdscr.addstr(" " * self.indicator_length + f" {option.label}\n")


class RightIndicatorHighlightOption(HighlightOptionBase):
    """Indicator option highlighter.

    This highlighter adds an indicator to the focused option.

    Example:

    ::

      Option 1 <
      Option 2
      Option 3
      ------------------
      Option 1
      Option 2 <
      Option 3
      ------------------
      Option 1
      Option 2
      Option 3 <

    """

    def __init__(self, indicator: str = "<") -> None:
        self.indicator = indicator
        self.indicator_length = len(indicator)

    def render_focused(self, stdscr: curses.window, option: Option):
        # set yellow color
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.addstr(f"{option.label} {self.indicator}\n", curses.color_pair(3))
        stdscr.chgat(-1, curses.color_pair(3))

    def render_not_focused(self, stdscr: curses.window, option: Option):
        stdscr.addstr(f" {option.label}\n")


class OuterIndicatorHighlightOption(HighlightOptionBase):
    """Indicator option highlighter.

    This highlighter adds an indicator to the focused option.

    Example:

    ::

      > Option 1 <
        Option 2
        Option 3
        ------------------
        Option 1
      > Option 2 <
        Option 3
        ------------------
        Option 1
        Option 2
      > Option 3 <

    """

    def __init__(self, outer_indicator: OuterIndicator = OuterIndicator(">", "<")):
        self.left_indicator = outer_indicator.left
        self.right_indicator = outer_indicator.right
        self.indicator_length = len(outer_indicator.left)

    def render_focused(self, stdscr: curses.window, option: Option):
        # set yellow color
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.addstr(
            f"{self.left_indicator} {option.label} {self.right_indicator}\n",
            curses.color_pair(3),
        )
        stdscr.chgat(-1, curses.color_pair(3))

    def render_not_focused(self, stdscr: curses.window, option: Option):
        stdscr.addstr(" " * self.indicator_length + f" {option.label}\n")
