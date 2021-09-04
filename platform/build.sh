#!/bin/bash

set -e

poetry install

if [[ -z "${CI}" ]]; then
  poetry run black .
else
  poetry run black --check .
fi


poetry run pytest --cov=src --cov-fail-under=96 --no-cov-on-fail --cov-branch tests
poetry run coverage html --directory reports/coverage/
