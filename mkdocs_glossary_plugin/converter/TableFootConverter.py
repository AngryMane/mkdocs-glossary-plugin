from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import TableFoot
except:
    TableFoot = Any

class TableFootConverter(BaseConverter):
    def __init__(self: "TableFootConverter") -> None:
        pass

CONVERTER_TABLE[TableFoot] = TableFootConverter()