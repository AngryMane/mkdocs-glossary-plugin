from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import TableBody
except:
    TableBody = Any


class TableBodyConverter(BaseConverter):
    def __init__(self: "TableBodyConverter") -> None:
        pass

    def convert(
        self: "BaseConverter", context: Context, target: TableBody
    ) -> List[Any]:
        return (
            super().convert(context, target) if context.replace_table_body else [target]
        )


CONVERTER_TABLE[TableBody] = TableBodyConverter()
