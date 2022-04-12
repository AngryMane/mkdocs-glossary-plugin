from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import CodeBlock
except:
    CodeBlock = Any


class CodeBlockConverter(BaseConverter):
    def __init__(self: "CodeBlockConverter") -> None:
        pass

    def convert(
        self: "BaseConverter", context: Context, target: CodeBlock
    ) -> List[Any]:
        return [target]


CONVERTER_TABLE[CodeBlock] = CodeBlockConverter()
