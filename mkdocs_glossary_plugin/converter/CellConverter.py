from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Cell
except:
    Cell = Any

class CellConverter(BaseConverter):
    def __init__(self: "CellConverter") -> None:
        pass

CONVERTER_TABLE[Cell] = CellConverter()