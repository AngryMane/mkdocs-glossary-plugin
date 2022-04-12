from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Attr
except:
    Attr = Any


class AttrConverter(BaseConverter):
    def __init__(self: "AttrConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: Attr) -> List[Any]:
        return [target]


CONVERTER_TABLE[Attr] = AttrConverter()
