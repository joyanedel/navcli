import curses

from navcli.structs import Option, View
from navcli.navigation import Navigation
import navcli.hightlights as hightlights


settings_view = View(
    title="Settings",
    options=[
        Option(label="Setting 1", action=lambda: print("Setting 1")),
        Option(label="Setting 2", action=lambda: print("Setting 2")),
        Option(label="Setting 3", action=lambda: print("Setting 3")),
        Option(
            label="Exit",
            action=lambda: print("Exiting..."),
            redirect=None,
        ),
    ],
    default_option=0,
)

game_view = View(
    title="Game",
    options=[
        Option(label="New Game", action=lambda: print("New Game")),
        Option(label="Load Game", action=lambda: print("Load Game")),
        Option(label="Save Game", action=lambda: print("Save Game")),
        Option(
            label="Exit",
            action=lambda: print("Exiting..."),
            redirect=None,
        ),
    ],
    default_option=0,
)

main_view = View(
    title="Select an option:",
    options=[
        Option(label="Game", action=lambda: print("Game"), redirect=game_view),
        Option(label="Option 2", action=lambda: print("Option 2")),
        Option(
            label="Settings", action=lambda: print("Option 3"), redirect=settings_view
        ),
        Option(
            label="Exit",
            action=lambda: print("Exiting..."),
            redirect=None,
        ),
    ],
    default_option=0,
)


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    navigation = Navigation(stdscr, main_view, hightlights.LeftArrowHighlightOption())
    navigation.navigate()


def run():
    curses.wrapper(main)
