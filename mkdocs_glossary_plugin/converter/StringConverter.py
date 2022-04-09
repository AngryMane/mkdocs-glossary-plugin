from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import String
except:
    String = Any

class StringConverter(BaseConverter):
    def __init__(self: "StringConverter") -> None:
        pass

CONVERTER_TABLE[String] = StringConverter()