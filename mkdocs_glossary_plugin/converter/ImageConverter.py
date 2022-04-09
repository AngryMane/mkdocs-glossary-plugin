from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Image
except:
    Image = Any

class ImageConverter(BaseConverter):
    def __init__(self: "ImageConverter") -> None:
        pass

CONVERTER_TABLE[Image] = ImageConverter()