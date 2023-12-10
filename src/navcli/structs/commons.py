"""Common structs for the navcli package."""

from typing import Callable, Union

from msgspec import Struct

from navcli.actions import Action


class Option(Struct):
    label: str
    action: Union[Callable, Action]


class View(Struct):
    options: list[Option]
    focused_option: int = 0
    title: str = "Select an option:"
