from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Target
except:
    Target = Any

class TargetConverter(BaseConverter):
    def __init__(self: "TargetConverter") -> None:
        pass

CONVERTER_TABLE[Target] = TargetConverter()