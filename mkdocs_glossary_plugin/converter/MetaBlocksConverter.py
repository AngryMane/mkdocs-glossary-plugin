from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MetaBlocks
except:
    MetaBlocks = Any


class MetaBlocksConverter(BaseConverter):
    def __init__(self: "MetaBlocksConverter") -> None:
        pass


CONVERTER_TABLE[MetaBlocks] = MetaBlocksConverter()
