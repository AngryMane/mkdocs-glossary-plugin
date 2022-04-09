import os
import sys
import time

from typing import List, Iterator, Any, Iterator
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

from mkdocs.structure.nav import Page, Navigation
from mkdocs.structure.files import File, Files
from mkdocs.livereload import LiveReloadServer

import pandoc
from pandoc.types import *

import markdown

from .converter import *
from .converter.BaseConverter import Word, Context
from .converter.PandocConverter import PandocConverter


class Const:
    GLOSSARY = 'glossary'

# See https://github.com/mkdocs/mkdocs/blob/1.2.2/docs/dev-guide/plugins.md


class GlossaryPlugin(BasePlugin):

    config_scheme = (
        # Subscripted generics cannot be used with class and instance checks
        ('glossary_dirs', config_options.Type(List, required=True)),
        ('input_format', config_options.Choice(choices=[
         'markdown', 'markdown_mmd', 'markdown_phpextra', 'markdown_strict'], default='markdown_phpextra')),
        ('output_format', config_options.Choice(choices=[
         'markdown', 'markdown_mmd', 'markdown_phpextra', 'markdown_strict'], default='markdown_phpextra')),
        ('enable_toc', config_options.Type(bool, default=True)),
        ('replace_emphasized_text', config_options.Type(bool, default=True)),
        ('replace_header', config_options.Type(bool, default=False)),
        ('replace_table_header', config_options.Type(bool, default=True)),
        ('replace_table_body', config_options.Type(bool, default=True)),
    )

    def __init__(self: "GlossaryPlugin") -> None:
        self.__glossary_dirs: List[str] = None
        self.__input_format: str = None
        self.__output_format: str = None
        self.__suffixes: List[str] = []
        self.__glossary: List[Word] = []

        self.__docs_dir: str = None

    # Global Events

    def on_config(self: "GlossaryPlugin", config: Config) -> Config:
        """
        The config event is the first event called on build and is run immediately after the user configuration is loaded and validated.
        Any alterations to the config should be made here.

        Parameters:
        : __config:__ global configuration object

        Returns:
        : global configuration object

        """
        self.__docs_dir = config['docs_dir']
        self.__glossary_dirs = [self.__docs_dir +
                                '/' + x for x in self.config['glossary_dirs']]
        self.__input_format = self.config["input_format"]
        self.__output_format = self.config["output_format"]
        self.__suffix = "md"

        # validation
        for invalid_glossary_dir in [x for x in self.__glossary_dirs if not self.validate_glossary_path(x)]:
            print(f"[WARNING]{invalid_glossary_dir} is not valid path.")
        self.__glossary_dirs = [
            x for x in self.__glossary_dirs if self.validate_glossary_path(x)]

        return config

    def on_files(self: "GlossaryPlugin", files: Files, config: Config) -> Files:
        """
        The files event is called after the files collection is populated from the docs_dir. 
        Use this event to add, remove, or alter files in the collection.
        Note that Page objects have not yet been associated with the file objects in the collection.
        Use Page Events to manipulate page specific data.

        Parameters:
        : __files:__ global files collection
        : __config:__ global configuration object

        Returns:
        : global files collection

        """
        md_files: List[File] = [x for x in files._files if x.abs_src_path.endswith(
            self.__suffix) and self.__is_in_glossary_dirs(x)]
        for file in md_files:
            words: List[Word] = self.__convert_file_to_words(config, file)
            self.__glossary.extend(words)
        self.__glossary.sort(key=lambda x: len(x.name), reverse=True)

        # validation
        for invalid_word in [x for x in self.__glossary if ' ' in x.name]:
            print(
                f"[WARNING]`{invalid_word.name}` includes spaces, but we can't support it.")
        self.__glossary_dirs = [
            x for x in self.__glossary if not ' ' in x.name]

        return files

    def on_nav(self: "GlossaryPlugin", nav: Navigation, config: Config, files: Files) -> Navigation:
        """
        The nav event is called after the site navigation is created and can be used to alter the site navigation.

        Parameters:
        : __nav:__ global navigation object
        : __config:__ global configuration object
        : __files:__ global files collection

        Returns:
        : global navigation object

        """
        return nav

    def on_env(self: "GlossaryPlugin", env: Any, config: Config, files: Files) -> Any:
        """
        The env event is called after the Jinja template environment is created and can be used to alter the Jinja environment.

        Parameters:
        : __env:__ global Jinja environment
        : __config:__ global configuration object
        : __files:__ global files collection

        Returns:
        : global Jinja Environment

        """
        return env

    def on_build_error(self: "GlossaryPlugin", error: Any) -> None:
        """
        The build_error event is called after an exception of any kind is caught by MkDocs during the build process.
        Use this event to clean things up before MkDocs terminates.
        Note that any other events which were scheduled to run after the error will have been skipped. See Handling Errors for more details.

        Parameters:
        : __error:__ exception raised

        """
        pass

    # Template Events

    # None

    # Page Events

    def on_page_markdown(self: "GlossaryPlugin", markdown: str, page: Page, config: Config, files: Files) -> str:
        """
        The page_markdown event is called after the page's markdown is loaded from file and can be used to alter the Markdown source text.
        The meta- data has been stripped off and is available as page.meta at this point.

        Parameters:
        : __markdown:__ Markdown source text of page as string
        : __page:__ `mkdocs.nav.Page` instance
        : __config:__ global configuration object
        : __files:__ global files collection

        Returns:
        : Markdown source text of page as string

        """
        doc: Pandoc = pandoc.read(markdown, format=self.__input_format)

        current_dir: str = os.path.dirname(
            self.__docs_dir + '/' + page.file.src_path)
        converter: PandocConverter = PandocConverter()
        doc = converter.convert(
            Context(self.config, self.__glossary, current_dir), doc)[0]
        markdown = pandoc.write(doc, format=self.__output_format)

        return markdown

    def validate_glossary_path(self: "GlossaryPlugin", glossary_path: str) -> bool:
        return \
            False if not glossary_path else\
            False if not os.path.exists(glossary_path) else\
            False if not os.path.isdir(glossary_path) else\
            True

    def __convert_file_to_words(self: "GlossaryPlugin", config: Config, file: File) -> List[Word]:
        result: List[Word] = []
        src_relative_path: str = self.__docs_dir + '/' + file.src_path

        word_names: str = [file.name] + self.__extract_alias_names(file)
        overlapped_word_names: List[str] = [
            x for x in word_names if x in [y.name for y in self.__glossary]]
        for overlapped_word_name in overlapped_word_names:
            print(f"[WARNING]{overlapped_word_name} is double registered.")

        word_names = [x for x in word_names if not x in [
            y.name for y in self.__glossary]]
        for word_name in word_names:
            current_word: Word = Word(word_name, src_relative_path)
            result.append(current_word)

        return result

    def __extract_alias_names(self: "GlossaryPlugin", file: File) -> List[str]:
        # NOTE
        # We should use the python pandoc modulce to parse meta deta in each files,
        # but we use the markdown module to parse becuase the python pandoc modulce seems not to be able to parse yaml block meta data at the head of the file.
        # mkdocs also depends on the markdown module, so actually this reference doesn't add new dependency.
        md = markdown.Markdown(extensions=['meta'])
        with open(file.abs_src_path, 'r') as f:
            data = f.read()
            md.convert(data)
        if not Const.GLOSSARY in md.Meta or not md.Meta[Const.GLOSSARY] or not md.Meta[Const.GLOSSARY][0]:
            return []
        return md.Meta[Const.GLOSSARY]

    def __is_in_glossary_dirs(self: "GlossaryPlugin", file: File) -> bool:
        matched_path: str = next(
            filter(lambda x: x in file.abs_src_path, self.__glossary_dirs), None)
        return True if matched_path else False
