from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Citation
except:
    Citation = Any

class CitationConverter(BaseConverter):
    def __init__(self: "CitationConverter") -> None:
        pass

CONVERTER_TABLE[Citation] = CitationConverter()