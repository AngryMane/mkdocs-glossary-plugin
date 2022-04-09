from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import LowerRoman
except:
    LowerRoman = Any

class LowerRomanConverter(BaseConverter):
    def __init__(self: "LowerRomanConverter") -> None:
        pass

CONVERTER_TABLE[LowerRoman] = LowerRomanConverter()