from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Caption
except:
    Caption = Any

class CaptionConverter(BaseConverter):
    def __init__(self: "CaptionConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: Caption) -> List[Any]:
        return [target]

CONVERTER_TABLE[Caption] = CaptionConverter()