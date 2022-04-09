from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Para
except:
    Para = Any

class ParaConverter(BaseConverter):
    def __init__(self: "ParaConverter") -> None:
        pass

CONVERTER_TABLE[Para] = ParaConverter()