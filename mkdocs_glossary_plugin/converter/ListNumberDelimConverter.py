from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ListNumberDelim
except:
    ListNumberDelim = Any


class ListNumberDelimConverter(BaseConverter):
    def __init__(self: "ListNumberDelimConverter") -> None:
        pass


CONVERTER_TABLE[ListNumberDelim] = ListNumberDelimConverter()
