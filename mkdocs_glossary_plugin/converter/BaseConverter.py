from typing import Any, List, Dict
from collections import namedtuple

from mkdocs.config import config_options, Config

Word = namedtuple('Word', ['name', 'source_path'])

class Context:

    def __init__(self: "Context", config: Config, glossary: List[Word], current_dir: str) -> None:
        self.glossary: List[Word] = glossary
        self.current_dir: str = current_dir

        self.enable_toc: bool = config['enable_toc']
        self.replace_emphasized_text: bool = config["replace_emphasized_text"]
        self.replace_header: bool = config["replace_header"]
        self.replace_table_header: bool = config["replace_table_header"]
        self.replace_table_body: bool = config["replace_table_body"]

class BaseConverter:
    CONVERTER_TABLE: dict = {}

    def __init__(self: "BaseConverter") -> None:
        pass

    def convert(self: "BaseConverter", context: Context, target: Any) -> List[Any]:
        converted_list = []
        for child_index, child in enumerate(target):
            if child is None:
                continue
            converted: List[Any] = CONVERTER_TABLE[type(child)].convert(context, child)
            if len(converted) == 1 and child == converted[0]:
                continue
            converted_list.append((child_index, converted)) 

        for child_index, converted in reversed(converted_list):
            target[child_index] = converted[0]
            target[child_index + 1:child_index + 1] = converted[1:]

        return [target]

CONVERTER_TABLE: Dict[Any, BaseConverter] = {}