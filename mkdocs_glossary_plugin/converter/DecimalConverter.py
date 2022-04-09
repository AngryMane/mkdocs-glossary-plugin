from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Decimal
except:
    Decimal = Any

class DecimalConverter(BaseConverter):
    def __init__(self: "DecimalConverter") -> None:
        pass

CONVERTER_TABLE[Decimal] = DecimalConverter()