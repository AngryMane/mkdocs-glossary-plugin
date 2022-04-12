from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import OrderedList
except:
    OrderedList = Any


class OrderedListConverter(BaseConverter):
    def __init__(self: "OrderedListConverter") -> None:
        pass


CONVERTER_TABLE[OrderedList] = OrderedListConverter()
