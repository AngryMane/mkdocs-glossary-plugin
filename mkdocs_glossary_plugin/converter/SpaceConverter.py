from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Space
except:
    Space = Any


class SpaceConverter(BaseConverter):
    def __init__(self: "SpaceConverter") -> None:
        pass


CONVERTER_TABLE[Space] = SpaceConverter()
