from setuptools import setup, find_packages

setup(
    name='mkdocs-glossary_plugin',
    version='0.1.0',
    description='A MkDocs plugin providing glossary',
    long_description='',
    keywords='mkdocs',
    url='',
    author='AngryMane',
    author_email='regulationdango@gmail.com',
    license='MIT',
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=1.0.3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-glossary-plugin = mkdocs_glossary_plugin.plugin:GlossaryPlugin'
        ]
    }
)