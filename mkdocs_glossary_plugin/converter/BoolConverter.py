from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Bool
except:
    Bool = Any

class BoolConverter(BaseConverter):
    def __init__(self: "BoolConverter") -> None:
        pass

CONVERTER_TABLE[Bool] = BoolConverter()