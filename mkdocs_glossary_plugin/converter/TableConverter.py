from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Table
except:
    Table = Any

class TableConverter(BaseConverter):
    def __init__(self: "TableConverter") -> None:
        pass

CONVERTER_TABLE[Table] = TableConverter()