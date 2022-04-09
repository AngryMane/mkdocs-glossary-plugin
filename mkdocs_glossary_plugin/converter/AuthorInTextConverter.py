from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List

import pandoc
from pandoc.types import *

try:
    from pandoc.types import AuthorInText
except:
    AuthorInText = Any

class AuthorInTextConverter(BaseConverter):
    def __init__(self: "AuthorInTextConverter") -> None:
        pass

CONVERTER_TABLE[AuthorInText] = AuthorInTextConverter()