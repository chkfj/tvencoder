#!/bin/sh
VENV=$1
echo $VENV
if [ -z $VENV ]; then
echo "usage: runinenv [virtualenv_path] CMDS"
  exit 1
fi
. ${VENV}/bin/activate
shift 1
echo "Executing $@ in ${VENV}"exec "$@"
$@

