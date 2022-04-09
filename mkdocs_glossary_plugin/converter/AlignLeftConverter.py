from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import AlignLeft
except:
    AlignLeft = Any

class AlignLeftConverter(BaseConverter):
    def __init__(self: "AlignLeftConverter") -> None:
        pass

CONVERTER_TABLE[AlignLeft] = AlignLeftConverter()