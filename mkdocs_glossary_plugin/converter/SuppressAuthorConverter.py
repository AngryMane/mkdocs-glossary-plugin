from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import SuppressAuthor
except:
    SuppressAuthor = Any


class SuppressAuthorConverter(BaseConverter):
    def __init__(self: "SuppressAuthorConverter") -> None:
        pass


CONVERTER_TABLE[SuppressAuthor] = SuppressAuthorConverter()
