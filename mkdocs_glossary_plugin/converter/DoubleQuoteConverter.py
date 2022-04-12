from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import DoubleQuote
except:
    DoubleQuote = Any


class DoubleQuoteConverter(BaseConverter):
    def __init__(self: "DoubleQuoteConverter") -> None:
        pass


CONVERTER_TABLE[DoubleQuote] = DoubleQuoteConverter()
