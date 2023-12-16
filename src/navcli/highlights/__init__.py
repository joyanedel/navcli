"""Module for highlight options."""

from .arrows import (
    LeftIndicatorHighlightOption,
    RightIndicatorHighlightOption,
    OuterIndicator,
    OuterIndicatorHighlightOption,
)
from .colors import ColorHighlightOption

# Left indicator highlighter
LEFT_INDICATOR_RIGHT_ARROW_HIGHTLIGHT = LeftIndicatorHighlightOption()
LEFT_INDICATOR_LEFT_ARROW_HIGHTLIGHT = LeftIndicatorHighlightOption("<")
LEFT_INDICATOR_BULLET_HIGHTLIGHT = LeftIndicatorHighlightOption("•")
LEFT_INDICATOR_DOT_HIGHTLIGHT = LeftIndicatorHighlightOption("·")

# Right indicator highlighter
RIGHT_INDICATOR_LEFT_ARROW_HIGHTLIGHT = RightIndicatorHighlightOption()
RIGHT_INDICATOR_RIGHT_ARROW_HIGHTLIGHT = RightIndicatorHighlightOption(">")

# Outer indicator highlighter
OUTER_INDICATOR_ARROWS_HIGHTLIGHT = OuterIndicatorHighlightOption(
    OuterIndicator("<", ">")
)
OUTER_INDICATOR_FILLED_ARROWS_HIGHTLIGHT = OuterIndicatorHighlightOption(
    OuterIndicator("◀", "▶")
)
OUTER_INDICATOR_BRACKETS_HIGHTLIGHT = OuterIndicatorHighlightOption(
    OuterIndicator("[", "]")
)


__all__ = [
    "LeftIndicatorHighlightOption",
    "ColorHighlightOption",
    # Left indicator highlighter
    "LEFT_INDICATOR_RIGHT_ARROW_HIGHTLIGHT",
    "LEFT_INDICATOR_LEFT_ARROW_HIGHTLIGHT",
    "LEFT_INDICATOR_BULLET_HIGHTLIGHT",
    "LEFT_INDICATOR_DOT_HIGHTLIGHT",
    # Right indicator highlighter
    "RIGHT_INDICATOR_LEFT_ARROW_HIGHTLIGHT",
    "RIGHT_INDICATOR_RIGHT_ARROW_HIGHTLIGHT",
    # Outer indicator highlighter
    "OUTER_INDICATOR_ARROWS_HIGHTLIGHT",
    "OUTER_INDICATOR_FILLED_ARROWS_HIGHTLIGHT",
    "OUTER_INDICATOR_BRACKETS_HIGHTLIGHT",
]
