from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import AlignCenter
except:
    AlignCenter = Any


class AlignCenterConverter(BaseConverter):
    def __init__(self: "AlignCenterConverter") -> None:
        pass


CONVERTER_TABLE[AlignCenter] = AlignCenterConverter()
