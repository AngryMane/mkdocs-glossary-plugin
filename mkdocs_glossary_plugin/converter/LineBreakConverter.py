from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import LineBreak
except:
    LineBreak = Any

class LineBreakConverter(BaseConverter):
    def __init__(self: "LineBreakConverter") -> None:
        pass

CONVERTER_TABLE[LineBreak] = LineBreakConverter()