from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Double
except:
    Double = Any


class DoubleConverter(BaseConverter):
    def __init__(self: "DoubleConverter") -> None:
        pass

    def convert(self: "DoubleConverter", context: Context, target: Double) -> List[Any]:
        return [target]


CONVERTER_TABLE[Double] = DoubleConverter()
