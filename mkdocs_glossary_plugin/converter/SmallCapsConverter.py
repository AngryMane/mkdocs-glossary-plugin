from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import SmallCaps
except:
    SmallCaps = Any


class SmallCapsConverter(BaseConverter):
    def __init__(self: "SmallCapsConverter") -> None:
        pass


CONVERTER_TABLE[SmallCaps] = SmallCapsConverter()
