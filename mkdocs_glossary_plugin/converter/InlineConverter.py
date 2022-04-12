from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Inline
except:
    Inline = Any


class InlineConverter(BaseConverter):
    def __init__(self: "InlineConverter") -> None:
        pass


CONVERTER_TABLE[Inline] = InlineConverter()
