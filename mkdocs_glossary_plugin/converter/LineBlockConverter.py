from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import LineBlock
except:
    LineBlock = Any

class LineBlockConverter(BaseConverter):
    def __init__(self: "LineBlockConverter") -> None:
        pass

CONVERTER_TABLE[LineBlock] = LineBlockConverter()