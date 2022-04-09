from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import DefaultStyle
except:
    DefaultStyle = Any

class DefaultStyleConverter(BaseConverter):
    def __init__(self: "DefaultStyleConverter") -> None:
        pass

CONVERTER_TABLE[DefaultStyle] = DefaultStyleConverter()