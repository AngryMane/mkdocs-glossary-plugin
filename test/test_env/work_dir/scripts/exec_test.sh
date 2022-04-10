PYTHON_VERSIONS=(
  3.7
  3.8
  3.9
  3.10
)

PANDOC_VERSIONS=(
  2.11
  2.12
  2.13
  2.14
  2.15
  2.16
  2.17
)

export SCRIPT_DIR=$(cd $(dirname $0); pwd)
for pandoc_version in ${PANDOC_VERSIONS[@]};
do
  export PANDOC_VERSION=${pandoc_version}
  dpkg -i pandoc-${pandoc_version}-1-amd64.deb
  for python_version in ${PYTHON_VERSIONS[@]};
  do
    export PYTHON_VERSION=$python_version
    bash ${SCRIPT_DIR}/exec_test_per_python_version.sh > /dev/null
  done
  dpkg -r pandoc 
done

