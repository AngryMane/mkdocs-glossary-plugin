from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Superscript
except:
    Superscript = Any

class SuperscriptConverter(BaseConverter):
    def __init__(self: "SuperscriptConverter") -> None:
        pass

CONVERTER_TABLE[Superscript] = SuperscriptConverter()