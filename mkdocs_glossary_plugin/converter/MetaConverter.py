from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Meta
except:
    Meta = Any


class MetaConverter(BaseConverter):
    def __init__(self: "MetaConverter") -> None:
        pass

    def convert(self: "StrConverter", context: Context, target: Str) -> List[Any]:
        return [target]


CONVERTER_TABLE[Meta] = MetaConverter()
