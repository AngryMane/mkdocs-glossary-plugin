from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import BlockQuote
except:
    BlockQuote = Any


class BlockQuoteConverter(BaseConverter):
    def __init__(self: "BlockQuoteConverter") -> None:
        pass


CONVERTER_TABLE[BlockQuote] = BlockQuoteConverter()
