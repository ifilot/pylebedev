#!/bin/bash

# set path to root
ROOT='//d//PROGRAMMING//PYTHON//pylebedev'
IMAGE='pylebedev-anaconda'

winpty docker run -i -t -v $ROOT://io -w //io -t $IMAGE .//docker_run_anaconda.sh
