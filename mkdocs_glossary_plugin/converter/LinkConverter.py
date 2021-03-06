from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Link
except:
    Link = Any


class LinkConverter(BaseConverter):
    def __init__(self: "LinkConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: Link) -> List[Any]:
        return [target]


CONVERTER_TABLE[Link] = LinkConverter()
