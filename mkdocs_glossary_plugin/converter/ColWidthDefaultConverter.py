from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ColWidthDefault
except:
    ColWidthDefault = Any

class ColWidthDefaultConverter(BaseConverter):
    def __init__(self: "ColWidthDefaultConverter") -> None:
        pass

CONVERTER_TABLE[ColWidthDefault] = ColWidthDefaultConverter()