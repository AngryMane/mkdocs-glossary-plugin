from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Math
except:
    Math = Any


class MathConverter(BaseConverter):
    def __init__(self: "MathConverter") -> None:
        pass

    def convert(self: "MathConverter", context: Context, target: Math) -> List[Any]:
        return (
            super().convert(context, target)
            if context.replace_math_element
            else [target]
        )


CONVERTER_TABLE[Math] = MathConverter()
