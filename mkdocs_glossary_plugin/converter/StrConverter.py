from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List
import os

import pandoc
from pandoc.types import *

try:
    from pandoc.types import Str
except:
    Str = Any


class StrConverter(BaseConverter):
    def __init__(self: "StrConverter") -> None:
        pass

    def convert(self: "StrConverter", context: Context, target: Str) -> List[Any]:
        if context.enable_toc and "[TOC]" == target[0]:
            return [RawInline(Format("html"), Text("[TOC]"))]
        result: List[Any] = self.__convert(context, target)
        return result if result else [target]

    def __convert(self: "StrConverter", context: Context, target: Str) -> List[Any]:
        result: List[Any] = []
        target_str: str = target[0]
        for word in context.glossary:
            start_index: int = target_str.find(word.name)
            if start_index == -1:
                continue
            if start_index != 0:
                result.extend(self.__convert(context, Str(target_str[0:start_index])))
            relative_path: str = os.path.relpath(word.source_path, context.current_dir)
            result.append(Link(("", [], []), [Str(word.name)], (relative_path, "")))
            if start_index + len(word.name) != len(target_str):
                result.extend(
                    self.__convert(
                        context, Str(target_str[start_index + len(word.name) :])
                    )
                )
            break
        return result if result else [target]


CONVERTER_TABLE[Str] = StrConverter()
