from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import QuoteType
except:
    QuoteType = Any


class QuoteTypeConverter(BaseConverter):
    def __init__(self: "QuoteTypeConverter") -> None:
        pass


CONVERTER_TABLE[QuoteType] = QuoteTypeConverter()
