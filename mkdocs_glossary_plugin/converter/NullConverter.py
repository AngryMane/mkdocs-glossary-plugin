from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Null
except:
    Null = Any

class NullConverter(BaseConverter):
    def __init__(self: "NullConverter") -> None:
        pass

CONVERTER_TABLE[Null] = NullConverter()