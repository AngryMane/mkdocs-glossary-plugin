from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import SoftBreak
except:
    SoftBreak = Any


class SoftBreakConverter(BaseConverter):
    def __init__(self: "SoftBreakConverter") -> None:
        pass


CONVERTER_TABLE[SoftBreak] = SoftBreakConverter()
