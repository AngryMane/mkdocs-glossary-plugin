from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import TableHead
except:
    TableHead = Any


class TableHeadConverter(BaseConverter):
    def __init__(self: "TableHeadConverter") -> None:
        pass

    def convert(
        self: "BaseConverter", context: Context, target: TableHead
    ) -> List[Any]:
        return (
            super().convert(context, target)
            if context.replace_table_header
            else [target]
        )


CONVERTER_TABLE[TableHead] = TableHeadConverter()
