from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import InlineMath
except:
    InlineMath = Any


class InlineMathConverter(BaseConverter):
    def __init__(self: "InlineMathConverter") -> None:
        pass

    def convert(
        self: "InlineMathConverter", context: Context, target: InlineMath
    ) -> List[Any]:
        return (
            super().convert(context, target)
            if context.replace_math_element
            else [target]
        )


CONVERTER_TABLE[InlineMath] = InlineMathConverter()
