from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MetaMap
except:
    MetaMap = Any


class MetaMapConverter(BaseConverter):
    def __init__(self: "MetaMapConverter") -> None:
        pass


CONVERTER_TABLE[MetaMap] = MetaMapConverter()
