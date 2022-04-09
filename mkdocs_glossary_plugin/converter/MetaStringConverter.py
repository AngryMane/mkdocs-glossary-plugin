from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MetaString
except:
    MetaString = Any

class MetaStringConverter(BaseConverter):
    def __init__(self: "MetaStringConverter") -> None:
        pass

CONVERTER_TABLE[MetaString] = MetaStringConverter()