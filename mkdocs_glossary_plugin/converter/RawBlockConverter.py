from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import RawBlock
except:
    RawBlock = Any


class RawBlockConverter(BaseConverter):
    def __init__(self: "RawBlockConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: RawBlock) -> List[Any]:
        # skip HTML block because of the processing speed
        return [target]


CONVERTER_TABLE[RawBlock] = RawBlockConverter()
