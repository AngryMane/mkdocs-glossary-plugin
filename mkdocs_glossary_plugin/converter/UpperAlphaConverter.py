from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import UpperAlpha
except:
    UpperAlpha = Any

class UpperAlphaConverter(BaseConverter):
    def __init__(self: "UpperAlphaConverter") -> None:
        pass

CONVERTER_TABLE[UpperAlpha] = UpperAlphaConverter()