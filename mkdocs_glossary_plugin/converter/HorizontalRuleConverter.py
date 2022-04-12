from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import HorizontalRule
except:
    HorizontalRule = Any


class HorizontalRuleConverter(BaseConverter):
    def __init__(self: "HorizontalRuleConverter") -> None:
        pass


CONVERTER_TABLE[HorizontalRule] = HorizontalRuleConverter()
