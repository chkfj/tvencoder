#!/bin/bash

export ENV_NAME=encode
export VIRTUALENV_PATH=/home/chinachu/env/$ENV_NAME
export PYTHON=$VIRTUALENV_PATH/bin/python

cd $(dirname $0)
${VIRTUALENV_PATH}/bin/rq-dashboard

