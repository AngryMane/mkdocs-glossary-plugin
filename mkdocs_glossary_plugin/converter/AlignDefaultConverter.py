from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import AlignDefault
except:
    AlignDefault = Any


class AlignDefaultConverter(BaseConverter):
    def __init__(self: "AlignDefaultConverter") -> None:
        pass


CONVERTER_TABLE[AlignDefault] = AlignDefaultConverter()
