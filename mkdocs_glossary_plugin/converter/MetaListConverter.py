from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import MetaList
except:
    MetaList = Any


class MetaListConverter(BaseConverter):
    def __init__(self: "MetaListConverter") -> None:
        pass


CONVERTER_TABLE[MetaList] = MetaListConverter()
