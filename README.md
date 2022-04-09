# mkdocs-glossary-plugin

This plugin provides a simple glossary feature for mkdocs.  

![demo](https://user-images.githubusercontent.com/27428050/162580047-b056fb41-1708-4e95-8708-70a15b1336e9.gif)


# What's useful?

When you are writing documents for your project, you maybe use some project-specific words.  
Of course, reader cannot understand these words without any explanation, but we want to avoid linking to all the places where these words are used.  

In these cases, this plugin can ...
- replace these words with a link to a specified page automatically
- control the details, such as not converting words contained in h1 or emph, but converting words contained in plain text.
- alias support. you can set alias for each word.


# How to install

```
python3 setup.py install
```


# Getting started
## Plugin configuration
Edit your mkdocs.yml file as follows.  

```
plugins:
  - mkdocs-glossary-plugin:
      glossary_dirs: ["foo", "bar"] # This plugin considers the md files in "docs/foo" and "docs/bar" as glossary files.
```

You can set some options, see Options section.


## Register glossary

For example, let's say you want to create a glossary of the word `x_word` .  
At first, You have to create `x_word.md` file like below as a glossary page for `x_word` .  

```
~/mkdocs_project/docs$ tree
.
├── foo
│   └── x_word.md
└── index.md
```

All that remains is for you to write freely in x_word.md!  
If you want to add an alias to `x_word`, set the glossary metadata at the beginning of the x_word.md file as follows.  

```
---
glossary: alias_word_a
glossary: alias_word_b
---

This is the glossary page for x_word!

```

That's all! Now, all the `x_word`, `alias_word_a` and `alias_word_b` in your project will be replaced with a link to x_word.md when building.


# Options

| Name                    | Necessary | Type      | Default             | Detail                                                                                                                                                         |
|-------------------------|-----------| ----------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| glossary_dirs           | required  | List[str] | None                | Specify the dirs containing the glossary md files. This plugin will only search for glossaries here. </br>**Please fill out with relative path from docs dir.**|
| input_format            | optional  | str       | `markdown_phpextra` | The input format of the markdown file. See [pandoc](https://pandoc.org/MANUAL.html#general-options)                                                            |
| output_format           | optional  | str       | `markdown_phpextra` | The output format of the markdown file. See [pandoc](https://pandoc.org/MANUAL.html#general-options)                                                           |
| enable_toc              | optional  | bool      | True                | If True, you can use table of contents(\[TOC\]) feature.                                                                                                       |
| replace_emphasized_text | optional  | bool      | True                | If True, emphaseized text includes specified word.                                                                                                             |
| replace_header          | optional  | bool      | False               | If True, h1,h2,.. includes specified word.                                                                                                                     |
| replace_table_header    | optional  | bool      | True                | If True, table header includes specified word.                                                                                                                 |
| replace_table_body      | optional  | bool      | True                | If True, table body includes specified word.                                                                                                                   |
