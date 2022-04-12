from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ListAttributes
except:
    ListAttributes = Any


class ListAttributesConverter(BaseConverter):
    def __init__(self: "ListAttributesConverter") -> None:
        pass


CONVERTER_TABLE[ListAttributes] = ListAttributesConverter()
