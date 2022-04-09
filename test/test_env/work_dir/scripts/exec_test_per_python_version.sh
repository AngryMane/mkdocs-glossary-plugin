#!/usr/bin/env bash

export PYTHOIN_BIN="python${PYTHON_VERSION}"

curl -sS https://bootstrap.pypa.io/get-pip.py | ${PYTHOIN_BIN}

apt-get -y install ${PYTHOIN_BIN}-distutils

${PYTHOIN_BIN} -m pip install zipp
${PYTHOIN_BIN} -m pip install mkdocs
${PYTHOIN_BIN} -m pip install mkdocs-material 
${PYTHOIN_BIN} -m pip install mkdocs-macros-plugin
${PYTHOIN_BIN} -m pip install pandoc

pushd ~/mkdocs_glossary_plugin
${PYTHOIN_BIN} setup.py install
popd




pushd ~/work_dir/test_document

# test case 01
rm -f mkdocs.yml
cp case_01.yml mkdocs.yml
${PYTHOIN_BIN} -m mkdocs build
cp -r site site_${PANDOC_VERSION}_${PYTHON_VERSION}_01

# test case 02
rm -f mkdocs.yml
cp case_02.yml mkdocs.yml
${PYTHOIN_BIN} -m mkdocs build
cp -r site site_${PANDOC_VERSION}_${PYTHON_VERSION}_02

popd