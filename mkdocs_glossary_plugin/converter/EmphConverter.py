from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Emph
except:
    Emph = Any


class EmphConverter(BaseConverter):
    def __init__(self: "EmphConverter") -> None:
        pass

    def convert(
        self: "BuiltInTypeConverter", context: Context, target: Any
    ) -> List[Any]:
        return (
            super().convert(context, target)
            if context.replace_emphasized_text
            else [target]
        )


CONVERTER_TABLE[Emph] = EmphConverter()
