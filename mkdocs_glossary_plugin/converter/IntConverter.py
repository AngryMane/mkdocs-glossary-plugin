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

    def convert(self: "IntConverter", context: Context, target: Int) -> List[Any]:
        return [target]


CONVERTER_TABLE[Int] = IntConverter()
