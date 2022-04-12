from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import ShortCaption
except:
    ShortCaption = Any


class ShortCaptionConverter(BaseConverter):
    def __init__(self: "ShortCaptionConverter") -> None:
        pass


CONVERTER_TABLE[ShortCaption] = ShortCaptionConverter()
