from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Code
except:
    Code = Any


class CodeConverter(BaseConverter):
    def __init__(self: "CodeConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: Code) -> List[Any]:
        return [target]


CONVERTER_TABLE[Code] = CodeConverter()
