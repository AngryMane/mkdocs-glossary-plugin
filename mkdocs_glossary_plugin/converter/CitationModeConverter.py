from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import CitationMode
except:
    CitationMode = Any


class CitationModeConverter(BaseConverter):
    def __init__(self: "CitationModeConverter") -> None:
        pass


CONVERTER_TABLE[CitationMode] = CitationModeConverter()
