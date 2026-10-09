from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MathType
except:
    MathType = Any


class MathTypeConverter(BaseConverter):
    def __init__(self: "MathTypeConverter") -> None:
        pass

    def convert(
        self: "MathTypeConverter", context: Context, target: MathType
    ) -> List[Any]:
        return (
            super().convert(context, target)
            if context.replace_math_element
            else [target]
        )


CONVERTER_TABLE[MathType] = MathTypeConverter()
