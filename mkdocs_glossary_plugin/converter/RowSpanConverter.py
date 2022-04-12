from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import RowSpan
except:
    RowSpan = Any


class RowSpanConverter(BaseConverter):
    def __init__(self: "RowSpanConverter") -> None:
        pass


CONVERTER_TABLE[RowSpan] = RowSpanConverter()
