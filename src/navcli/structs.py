from typing import Union, Callable

from msgspec import Struct

from navcli.actions.base import Action


class Option(Struct):
    label: str
    action: Union[Callable, Action]


class View(Struct):
    options: list[Option]
    focused_option: int = 0
    title: str = "Select an option:"
