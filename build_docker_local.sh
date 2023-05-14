#!/bin/bash

# clean any earlier distributions
rm -rvf build/*
rm -vf dist/*.whl wheelhouse/*.whl
rm -rvf *.egg-info

# set path and image
ROOT='//d//PROGRAMMING//PYTHON//pylebedev'
IMAGE='pylebedev-pypi'

# run pypi local
winpty docker run -i -t -v $ROOT://io -w //io $IMAGE .//deploy//docker_run_pypi.sh

# set path and image
ROOT='//d//PROGRAMMING//PYTHON//pylebedev'
IMAGE='pylebedev-anaconda'

# run anaconda build local
winpty docker run -i -t -v $ROOT://io -w //io -t $IMAGE .//deploy//docker_run_anaconda.sh
