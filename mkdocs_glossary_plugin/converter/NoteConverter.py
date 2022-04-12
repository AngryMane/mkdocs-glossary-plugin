from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Note
except:
    Note = Any


class NoteConverter(BaseConverter):
    def __init__(self: "NoteConverter") -> None:
        pass


CONVERTER_TABLE[Note] = NoteConverter()
