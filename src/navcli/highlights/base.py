"""Base class for option highlighters."""

import curses
from abc import ABC, abstractmethod

from navcli.structs import Option


class HighlightOptionBase(ABC):
    @abstractmethod
    def render_focused(self, stdscr: curses.window, option: Option):
        """Render the option that is currently focused.

        This method should be implemented by the child class.

        Parameters:
        ----------
        stdscr: curses.window
            The curses window object.
        option: Option
            The option that is currently focused.
        """
        pass

    @abstractmethod
    def render_not_focused(self, stdscr: curses.window, option: Option):
        """Render the option that is not currently focused.

        This method should be implemented by the child class.

        Parameters:
        ----------
        stdscr: curses.window
            The curses window object.
        option: Option
            The option that is not currently focused.
        """
        pass

    def render(self, stdscr: curses.window, option: Option, is_focused: bool):
        """Render the option.

        Parameters:
        ----------
        stdscr: curses.window
            The curses window object.
        option: Option
            The option to be rendered.
        is_focused: bool
            Whether the option is currently focused or not.
        """

        if is_focused:
            self.render_focused(stdscr, option)
        else:
            self.render_not_focused(stdscr, option)


class DefaultHighlightOption(HighlightOptionBase):
    """Default option highlighter."""

    def render_focused(self, stdscr: curses.window, option: Option):
        # set black color
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        stdscr.addstr(f"{option.label}\n", curses.color_pair(1))

    def render_not_focused(self, stdscr: curses.window, option: Option):
        stdscr.addstr(f"{option.label}\n")
