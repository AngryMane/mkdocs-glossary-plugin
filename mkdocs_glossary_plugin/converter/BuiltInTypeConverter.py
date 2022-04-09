from .BaseConverter import BaseConverter, CONVERTER_TABLE, Context, Word
from typing import Any, List, Dict, Tuple

import pandoc
from pandoc.types import *

class BuiltInTypeConverter(BaseConverter):
    def __init__(self: "BuiltInTypeConverter") -> None:
        pass

    def convert(self: "BuiltInTypeConverter", context: Context, target: Any) -> List[Any]:
        if isinstance(target, list):
            return self.convert_list(context, target)
        elif isinstance(target, dict):
            return self.convert_dict(context, target)
        elif isinstance(target, tuple):
            return self.convert_tuple(context, target)
        elif isinstance(target, int):
            pass
        else:
            pass
        return [target]

    def convert_list(self: "PandocConverter", context: Context, target: List[Any]) -> List[Any]:
        converted_list = []
        for index, child in enumerate(target):
            converted = CONVERTER_TABLE[type(child)].convert(context, child)
            if len(converted) == 1 and child == converted[0]:
                continue
            converted_list.append((index, converted)) 
        for child_index, converted in reversed(converted_list):
            target[child_index] = converted[0]
            target[child_index + 1:child_index + 1] = converted[1:]
        return [target]

    def convert_dict(self: "PandocConverter", context: Context, target: Dict[Any, Any]) -> List[Any]:
        converted_list = []
        for index, child in enumerate(target.items()):
            converted = CONVERTER_TABLE[type(child)].convert(context, child)
            if len(converted) == 1 and child == converted[0]:
                continue
            converted_list.append((index, converted)) 
        for child_index, converted in reversed(converted_list):
            target[child_index] = converted[0]
            target[child_index + 1:child_index + 1] = converted[1:]
        return [target]

    def convert_tuple(self: "PandocConverter", context: Context, target: Tuple[Any, Any]) -> List[Any]:
        converted_list = []
        for index, child in enumerate(target):
            converted = CONVERTER_TABLE[type(child)].convert(context, child)
            if len(converted) == 1 and child == converted[0]:
                continue
            converted_list.append((index, converted)) 
        for child_index, converted in reversed(converted_list):
            target[child_index] = converted[0]
            target[child_index + 1:child_index + 1] = converted[1:]
        return [target]

CONVERTER_TABLE[dict] = BuiltInTypeConverter()
CONVERTER_TABLE[list] = BuiltInTypeConverter()
CONVERTER_TABLE[tuple] = BuiltInTypeConverter()
CONVERTER_TABLE[int] = BuiltInTypeConverter()