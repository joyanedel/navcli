import curses
from queue import Queue
from .hightlights import HighlightOptionBase, DefaultHighlightOption
from .structs import Option, View


class Navigation:
    def __init__(
        self,
        stdscr: curses.window,
        view: View,
        highlight_option: HighlightOptionBase = DefaultHighlightOption(),
    ):
        self.stdscr = stdscr
        self.view = view
        self.current_option = view.default_option
        self.navigation_historial: Queue[View] = Queue()

        self.highlight_option = highlight_option

    def display_options(self):
        """Display the options of the current view."""

        self.stdscr.clear()
        self.stdscr.addstr(f"{self.view.title}\n\n")

        for i, option in enumerate(self.view.options):
            if i == self.current_option:
                self.highlight_option.render(self.stdscr, option)
            else:
                self.stdscr.addstr(f"{option.label}\n")

        self.stdscr.refresh()

    def navigate(self):
        """Navigate through the views.

        The navigation is done using the arrow keys, the enter key and the backspace key.

        The arrow keys are used to move the cursor up and down the options.
        The enter key is used to select an option.
        The backspace key is used to go back to the previous view.

        The navigation is done in a loop until the user presses the exit key or q.
        """
        self.display_options()

        while True:
            key = self.stdscr.getch()

            if key == curses.KEY_UP:
                self.current_option = max(0, self.current_option - 1)
                self.display_options()
            elif key == curses.KEY_DOWN:
                self.current_option = min(
                    len(self.view.options) - 1, self.current_option + 1
                )
                self.display_options()
            elif key == curses.KEY_ENTER or key in [10, 13]:
                option = self.view.options[self.current_option]

                if option.redirect:
                    self.navigation_historial.put(self.view)
                    self.view = option.redirect
                    self.current_option = self.view.default_option
                    self.display_options()
                else:
                    option.action()
                    break
            elif key == curses.KEY_BACKSPACE or key == 127:
                if self.navigation_historial.empty():
                    break

                self.view = self.navigation_historial.get()
                self.current_option = self.view.default_option
                self.display_options()

            elif key == curses.KEY_RESIZE:
                self.stdscr.clear()
                self.stdscr.refresh()
                self.display_options()

            elif key == ord("q") or key == ord("Q") or key == 27:
                break

    def run(self):
        self.navigate()
        self.stdscr.clear()
        self.stdscr.refresh()
        curses.endwin()
