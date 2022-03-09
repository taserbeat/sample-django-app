#!/bin/bash

readonly VENV_DIR="./.venv/"
readonly PIPFILE_NAME="Pipfile"
readonly PIPFILE_LOCK_NAME="Pipfile.lock"

cd $(dirname $0)

if [ -e ${VENV_DIR} ]; then
  rm -r ${VENV_DIR}
fi

export PIPENV_VENV_IN_PROJECT=true

if [ -e ${PIPFILE_LOCK_NAME} ]; then
  echo "Now running 'pipenv sync --dev'"
  pipenv sync --dev
elif [ -e ${PIPFILE_NAME} ]; then
  echo "Now running 'pipenv install --dev'"
  pipenv install --dev
else
  echo "${PIPFILE_NAME} and ${PIPFILE_LOCK_NAME} does not exist."
fi
