from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import LowerAlpha
except:
    LowerAlpha = Any

class LowerAlphaConverter(BaseConverter):
    def __init__(self: "LowerAlphaConverter") -> None:
        pass

CONVERTER_TABLE[LowerAlpha] = LowerAlphaConverter()