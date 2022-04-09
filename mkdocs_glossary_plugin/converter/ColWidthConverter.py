from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ColWidth
except:
    ColWidth = Any

class ColWidthConverter(BaseConverter):
    def __init__(self: "ColWidthConverter") -> None:
        pass

CONVERTER_TABLE[ColWidth] = ColWidthConverter()