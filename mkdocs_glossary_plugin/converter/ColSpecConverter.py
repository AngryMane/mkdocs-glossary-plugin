from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ColSpec
except:
    ColSpec = Any

class ColSpecConverter(BaseConverter):
    def __init__(self: "ColSpecConverter") -> None:
        pass

CONVERTER_TABLE[ColSpec] = ColSpecConverter()