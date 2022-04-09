from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import DefinitionList
except:
    DefinitionList = Any

class DefinitionListConverter(BaseConverter):
    def __init__(self: "DefinitionListConverter") -> None:
        pass

CONVERTER_TABLE[DefinitionList] = DefinitionListConverter()