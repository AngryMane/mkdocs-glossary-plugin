from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Div
except:
    Div = Any


class DivConverter(BaseConverter):
    def __init__(self: "DivConverter") -> None:
        pass


CONVERTER_TABLE[Div] = DivConverter()
