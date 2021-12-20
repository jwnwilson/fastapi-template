#!/usr/bin/env bash

set -e
set -x

# assumed docker image folder
APP_FOLDER=task

cd ..

mypy ${APP_FOLDER}
black ${APP_FOLDER}
isort ${APP_FOLDER}