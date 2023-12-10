import curses
from queue import Queue

from navcli.hightlights import HighlightOptionBase, DefaultHighlightOption
from navcli.structs import View
from navcli.actions import Quit, Redirect
from navcli.exceptions import UnexpectedActionException


class Navigation:
    def __init__(
        self,
        stdscr: curses.window,
        view: View,
        highlight_option: HighlightOptionBase = DefaultHighlightOption(),
    ):
        self.stdscr = stdscr
        self.view = view
        self.focused_option = view.focused_option
        self.navigation_historial: Queue[View] = Queue()

        self.highlight_option = highlight_option

    def display_options(self):
        """Display the options of the current view."""

        self.stdscr.clear()
        self.stdscr.addstr(f"{self.view.title}\n\n")

        for i, option in enumerate(self.view.options):
            is_focused = i == self.focused_option
            self.highlight_option.render(self.stdscr, option, is_focused)

        self.stdscr.refresh()

    def loop(self):
        """Loop through the options of the current view.

        The navigation is done using the arrow keys, the enter key and the backspace key.

        The arrow keys are used to move the cursor up and down the options.
        The enter key is used to select an option.
        The backspace key is used to go back to the previous view.

        The navigation is done in a loop until the user presses the exit key or q.

        Raises:
        -------
        UnexpectedActionException
            If the action of the selected option is not valid.
        """

        while True:
            self.display_options()
            key = self.stdscr.getch()

            if key == curses.KEY_UP:
                self.focused_option = max(0, self.focused_option - 1)

            elif key == curses.KEY_DOWN:
                self.focused_option = min(
                    len(self.view.options) - 1, self.focused_option + 1
                )

            elif key == curses.KEY_ENTER or key in [10, 13]:
                option = self.view.options[self.focused_option]

                if callable(option.action):
                    option.action()
                    continue

                elif isinstance(option.action, Quit):
                    break

                elif isinstance(option.action, Redirect):
                    self.navigation_historial.put(self.view)
                    self.view = option.action.view
                    self.focused_option = self.view.focused_option
                    continue

                raise UnexpectedActionException(option.action)

            elif key == curses.KEY_BACKSPACE or key == 127:
                if self.navigation_historial.empty():
                    self.stdscr.clear()
                    self.stdscr.refresh()
                    self.stdscr.addstr(
                        "No previous views.\nPlease press any key to continue."
                    )
                    self.stdscr.getch()
                    continue

                self.view = self.navigation_historial.get()
                self.focused_option = self.view.focused_option

            elif key == curses.KEY_RESIZE:
                self.stdscr.clear()
                self.stdscr.refresh()

            elif key == ord("q") or key == ord("Q") or key == 27:
                break

    def navigate(self):
        """Navigate through the views.

        The navigation is done using the arrow keys, the enter key and the backspace key.

        The arrow keys are used to move the cursor up and down the options.
        The enter key is used to select an option.
        The backspace key is used to go back to the previous view.

        The navigation is done in a loop until the user presses the exit key or q.
        """
        self.display_options()
        self.loop()

    def run(self):
        self.navigate()
        self.stdscr.clear()
        self.stdscr.refresh()
        curses.endwin()
