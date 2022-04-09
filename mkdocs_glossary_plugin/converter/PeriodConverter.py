from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Period
except:
    Period = Any

class PeriodConverter(BaseConverter):
    def __init__(self: "PeriodConverter") -> None:
        pass

CONVERTER_TABLE[Period] = PeriodConverter()