from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Plain
except:
    Plain = Any

class PlainConverter(BaseConverter):
    def __init__(self: "PlainConverter") -> None:
        pass

CONVERTER_TABLE[Plain] = PlainConverter()