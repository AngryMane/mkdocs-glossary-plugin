from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Example
except:
    Example = Any


class ExampleConverter(BaseConverter):
    def __init__(self: "ExampleConverter") -> None:
        pass


CONVERTER_TABLE[Example] = ExampleConverter()
