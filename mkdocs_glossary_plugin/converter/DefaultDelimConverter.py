from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import DefaultDelim
except:
    DefaultDelim = Any

class DefaultDelimConverter(BaseConverter):
    def __init__(self: "DefaultDelimConverter") -> None:
        pass

CONVERTER_TABLE[DefaultDelim] = DefaultDelimConverter()