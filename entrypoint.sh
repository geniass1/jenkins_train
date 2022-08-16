#!/bin/sh


echo "Starting run linters"

flake8
black .
mypy .

exec "$@"