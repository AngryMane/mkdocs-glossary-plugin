from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Int
except:
    Int = Any


class IntConverter(BaseConverter):
    def __init__(self: "IntConverter") -> None:
        pass

    def convert(
        self: "PandocConverter", context: Context, target: List[Any]
    ) -> List[Any]:
        return [target]


CONVERTER_TABLE[Int] = IntConverter()
