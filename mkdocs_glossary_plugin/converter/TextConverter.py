from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Text
except:
    Text = Any

class TextConverter(BaseConverter):
    def __init__(self: "TextConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: Any) -> List[Any]:
        return [target]


CONVERTER_TABLE[Text] = TextConverter()