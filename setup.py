from setuptools import setup, find_packages
from subprocess import run, CompletedProcess
from os import path

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='mkdocs-glossary_plugin',
    version='0.1.1',
    description='This plugin automatically turns specific words into links to specific pages.',
    long_description_content_type="text/markdown",
    long_description=read("README.md"),
    keywords='mkdocs',
    url='https://github.com/AngryMane/mkdocs-glossary-plugin',
    author='AngryMane',
    author_email='regulationdango@gmail.com',
    license='MIT',
    python_requires='>=3.7',
    install_requires=[
        'mkdocs>=1.0.3',
        'pandoc',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Topic :: Documentation',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-glossary-plugin = mkdocs_glossary_plugin.plugin:GlossaryPlugin'
        ]
    },
)

def check_pandoc():
    completed_process: CompletedProcess = run(
        ['which', 'pandoc'], capture_output=True, text=True)
    which_pandoc_result: str = completed_process.stdout
    if not which_pandoc_result:
        print(
            '\033[31m' + "[WARNING]This plugin needs pandoc>=2.11. Please install pandoc." + '\033[0m')
        return
    completed_process: CompletedProcess = run(
        ['pandoc', '--version'], capture_output=True, text=True)
    pandoc_verson_result: str = completed_process.stdout
    pandoc_version_text: str = pandoc_verson_result.splitlines()[0]
    pandoc_version_text: str = pandoc_version_text.split()[1]

    major_version: int = int(pandoc_version_text.split('.')[0])
    minor_version: int = int(pandoc_version_text.split('.')[1])
    if major_version < 2 or major_version == 2 and minor_version < 11:
        print(
            '\033[31m' + f"[WARNING]The version of your pandoc is {pandoc_version_text}, but this plugin needs 2.11 or later." + '\033[0m')
        return

check_pandoc()
