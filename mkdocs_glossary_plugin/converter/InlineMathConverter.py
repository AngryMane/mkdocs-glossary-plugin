from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import InlineMath
except:
    InlineMath = Any


class InlineMathConverter(BaseConverter):
    def __init__(self: "InlineMathConverter") -> None:
        pass


CONVERTER_TABLE[InlineMath] = InlineMathConverter()
