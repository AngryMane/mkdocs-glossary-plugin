from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import OneParen
except:
    OneParen = Any

class OneParenConverter(BaseConverter):
    def __init__(self: "OneParenConverter") -> None:
        pass

CONVERTER_TABLE[OneParen] = OneParenConverter()