from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MetaValue
except:
    MetaValue = Any

class MetaValueConverter(BaseConverter):
    def __init__(self: "MetaValueConverter") -> None:
        pass

CONVERTER_TABLE[MetaValue] = MetaValueConverter()