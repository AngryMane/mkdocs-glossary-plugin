from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MetaBool
except:
    MetaBool = Any

class MetaBoolConverter(BaseConverter):
    def __init__(self: "MetaBoolConverter") -> None:
        pass

CONVERTER_TABLE[MetaBool] = MetaBoolConverter()