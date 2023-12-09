from typing import Callable, Optional

from msgspec import Struct


class Option(Struct):
    label: str
    action: Callable
    redirect: Optional["View"] = None


class View(Struct):
    options: list[Option]
    default_option: int = 0
    title: str = "Select an option:"
