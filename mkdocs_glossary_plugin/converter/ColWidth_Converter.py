from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ColWidth_
except:
    ColWidth_ = Any

class ColWidth_Converter(BaseConverter):
    def __init__(self: "ColWidth_Converter") -> None:
        pass

CONVERTER_TABLE[ColWidth_] = ColWidth_Converter()