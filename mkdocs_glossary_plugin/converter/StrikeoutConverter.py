from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Strikeout
except:
    Strikeout = Any

class StrikeoutConverter(BaseConverter):
    def __init__(self: "StrikeoutConverter") -> None:
        pass

CONVERTER_TABLE[Strikeout] = StrikeoutConverter()