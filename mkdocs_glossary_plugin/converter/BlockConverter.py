from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Block
except:
    Block = Any

class BlockConverter(BaseConverter):
    def __init__(self: "BlockConverter") -> None:
        pass

CONVERTER_TABLE[Block] = BlockConverter()