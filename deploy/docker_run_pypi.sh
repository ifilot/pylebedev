#!/bin/bash

set -e -u -x

# Compile wheels
/opt/python/cp39*/bin/python /io/setup.py bdist_wheel

set -e -u -x

# Install packages and test
for PYBIN in /opt/python/cp3[9]*/bin; do
    "${PYBIN}/python" -m pip install numpy nose
    "${PYBIN}/pip" install pylebedev --no-index -f /io/dist
    (cd "$HOME"; "${PYBIN}/nosetests" --verbose /io/tests/*.py)
done
