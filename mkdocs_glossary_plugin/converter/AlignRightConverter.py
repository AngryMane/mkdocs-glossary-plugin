from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import AlignRight
except:
    AlignRight = Any


class AlignRightConverter(BaseConverter):
    def __init__(self: "AlignRightConverter") -> None:
        pass


CONVERTER_TABLE[AlignRight] = AlignRightConverter()
