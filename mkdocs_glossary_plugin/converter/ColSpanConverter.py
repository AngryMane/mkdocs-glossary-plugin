from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ColSpan
except:
    ColSpan = Any

class ColSpanConverter(BaseConverter):
    def __init__(self: "ColSpanConverter") -> None:
        pass

CONVERTER_TABLE[ColSpan] = ColSpanConverter()