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
            return [RawInline(Format("html"), Text("[TOC]"))]  # type: ignore
        result: List[Any] = self.__convert(context, target)
        return result if result else [target]

    def __convert(self: "StrConverter", context: Context, target: Str) -> List[Any]:
        result: List[Any] = []
        target_str: str = target[0]
        for word in context.glossary:
            matching_word_name: str = (
                word.name if context.is_case_sensitive else word.name.lower()
            )
            matching_target_str: str = (
                target_str if context.is_case_sensitive else target_str.lower()
            )

            start_index: int = matching_target_str.find(matching_word_name)
            if start_index == -1:
                continue
            if start_index != 0:
                result.extend(self.__convert(context, Str(target_str[0:start_index])))

            link_str: Str = Str(target_str[start_index : start_index + len(word.name)])
            relative_path: str = os.path.relpath(word.source_path, context.current_dir)
            result.append(Link(("", [], []), [link_str], (relative_path, "")))  # type: ignore

            if start_index + len(word.name) != len(target_str):
                result.extend(
                    self.__convert(
                        context, Str(target_str[start_index + len(word.name) :])
                    )
                )
            break
        return result if result else [target]


CONVERTER_TABLE[Str] = StrConverter()
