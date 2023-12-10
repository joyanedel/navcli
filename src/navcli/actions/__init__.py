"""Module that defines application actions.

Actions are used to define what happens when an option is selected.
"""

from .quit import Quit
from .redirect import Redirect

__all__ = ["Quit", "Redirect"]
