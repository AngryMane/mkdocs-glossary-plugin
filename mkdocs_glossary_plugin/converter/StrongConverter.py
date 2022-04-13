from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Strong
except:
    Strong = Any


class StrongConverter(BaseConverter):
    def __init__(self: "StrongConverter") -> None:
        pass

    def convert(self: "StrongConverter", context: Context, target: Strong) -> List[Any]:
        return (
            super().convert(context, target)
            if context.replace_emphasized_text
            else [target]
        )


CONVERTER_TABLE[Strong] = StrongConverter()
