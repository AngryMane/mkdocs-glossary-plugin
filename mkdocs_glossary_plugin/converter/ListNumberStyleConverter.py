from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ListNumberStyle
except:
    ListNumberStyle = Any

class ListNumberStyleConverter(BaseConverter):
    def __init__(self: "ListNumberStyleConverter") -> None:
        pass

CONVERTER_TABLE[ListNumberStyle] = ListNumberStyleConverter()