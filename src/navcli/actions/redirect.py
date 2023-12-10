"""Redirect to another view."""

from typing import TypeVar
from msgspec import Struct

from .base import Action

View = TypeVar("View")


class Redirect(Action, Struct):
    """Redirect to another view."""

    view: View
