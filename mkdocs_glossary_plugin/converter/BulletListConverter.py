from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import BulletList
except:
    BulletList = Any

class BulletListConverter(BaseConverter):
    def __init__(self: "BulletListConverter") -> None:
        pass

CONVERTER_TABLE[BulletList] = BulletListConverter()