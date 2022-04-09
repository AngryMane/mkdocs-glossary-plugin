from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Pandoc
except:
    Pandoc = Any

class PandocConverter(BaseConverter):
    def __init__(self: "PandocConverter") -> None:
        pass

CONVERTER_TABLE[Pandoc] = PandocConverter()