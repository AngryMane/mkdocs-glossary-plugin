from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Row
except:
    Row = Any

class RowConverter(BaseConverter):
    def __init__(self: "RowConverter") -> None:
        pass

CONVERTER_TABLE[Row] = RowConverter()