"""Module that defines application actions.

Actions are used to define what happens when an option is selected.
"""

from .base import Action
from .commons import Quit as __Quit
from .commons import Redirect

QUIT = __Quit()

__all__ = ["QUIT", "Redirect", "Action"]
