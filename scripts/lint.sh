#!/usr/bin/env bash

set -e
set -x

cd ../app

mypy .
black .
isort .