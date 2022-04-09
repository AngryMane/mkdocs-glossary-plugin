from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Format
except:
    Format = Any

class FormatConverter(BaseConverter):
    def __init__(self: "FormatConverter") -> None:
        pass

CONVERTER_TABLE[Format] = FormatConverter()