from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import NormalCitation
except:
    NormalCitation = Any

class NormalCitationConverter(BaseConverter):
    def __init__(self: "NormalCitationConverter") -> None:
        pass

CONVERTER_TABLE[NormalCitation] = NormalCitationConverter()