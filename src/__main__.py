import curses

from navcli.structs import Option, View
from navcli.actions import Redirect, QUIT
from navcli.navigation import Navigation
from navcli.highlights import *


settings_view = View(
    title="Settings",
    options=[
        Option(label="Setting 1", action=lambda: print("Setting 1")),
        Option(label="Setting 2", action=lambda: print("Setting 2")),
        Option(label="Setting 3", action=lambda: print("Setting 3")),
        Option(label="Exit", action=QUIT),
    ],
    focused_option=0,
)

game_view = View(
    title="Game",
    options=[
        Option(label="New Game", action=lambda: print("New Game")),
        Option(label="Load Game", action=lambda: print("Load Game")),
        Option(label="Save Game", action=lambda: print("Save Game")),
        Option(label="Exit", action=QUIT),
    ],
    focused_option=0,
)

main_view = View(
    title="Select an option:",
    options=[
        Option(label="Game", action=Redirect(game_view)),
        Option(label="Option 2", action=lambda: print("Option 2")),
        Option(label="Settings", action=Redirect(settings_view)),
        Option(label="Exit", action=QUIT),
    ],
    focused_option=0,
)


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    navigation = Navigation(stdscr, main_view, OUTER_INDICATOR_FILLED_ARROWS_HIGHTLIGHT)
    navigation.navigate()


def run():
    curses.wrapper(main)
