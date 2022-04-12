from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import RawInline
except:
    RawInline = Any


class RawInlineConverter(BaseConverter):
    def __init__(self: "RawInlineConverter") -> None:
        pass


CONVERTER_TABLE[RawInline] = RawInlineConverter()
