from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import TwoParens
except:
    TwoParens = Any

class TwoParensConverter(BaseConverter):
    def __init__(self: "TwoParensConverter") -> None:
        pass

CONVERTER_TABLE[TwoParens] = TwoParensConverter()