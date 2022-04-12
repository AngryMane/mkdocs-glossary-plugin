from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Alignment
except:
    Alignment = Any


class AlignmentConverter(BaseConverter):
    def __init__(self: "AlignmentConverter") -> None:
        pass


CONVERTER_TABLE[Alignment] = AlignmentConverter()
