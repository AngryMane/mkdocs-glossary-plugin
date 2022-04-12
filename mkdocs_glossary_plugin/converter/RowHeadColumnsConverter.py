from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import RowHeadColumns
except:
    RowHeadColumns = Any


class RowHeadColumnsConverter(BaseConverter):
    def __init__(self: "RowHeadColumnsConverter") -> None:
        pass


CONVERTER_TABLE[RowHeadColumns] = RowHeadColumnsConverter()
