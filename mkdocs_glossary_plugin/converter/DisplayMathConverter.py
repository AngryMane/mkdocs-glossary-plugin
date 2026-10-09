from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import DisplayMath
except:
    DisplayMath = Any


class DisplayMathConverter(BaseConverter):
    def __init__(self: "DisplayMathConverter") -> None:
        pass

    def convert(
        self: "DisplayMathConverter", context: Context, target: DisplayMath
    ) -> List[Any]:
        return (
            super().convert(context, target)
            if context.replace_math_element
            else [target]
        )


CONVERTER_TABLE[DisplayMath] = DisplayMathConverter()
