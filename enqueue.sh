#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: enqueue.sh m2ts_path json"
    exit 1
fi

export ENV_NAME=encode
export VIRTUALENV_PATH=/home/chinachu/env/$ENV_NAME
export PYTHON=$VIRTUALENV_PATH/bin/python

BASE=/home/chinachu/src/tvencoder
$PYTHON ${BASE}/enqueue.py $1
