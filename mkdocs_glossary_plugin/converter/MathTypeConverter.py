from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MathType
except:
    MathType = Any

class MathTypeConverter(BaseConverter):
    def __init__(self: "MathTypeConverter") -> None:
        pass

CONVERTER_TABLE[MathType] = MathTypeConverter()