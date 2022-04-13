from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Header
except:
    Header = Any


class HeaderConverter(BaseConverter):
    def __init__(self: "HeaderConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: Header) -> List[Any]:
        return super().convert(context, target) if context.replace_header else [target]  # type: ignore


CONVERTER_TABLE[Header] = HeaderConverter()
