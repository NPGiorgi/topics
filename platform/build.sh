#!/bin/bash

set -e

poetry install

if [[ -z "${CI}" ]]; then
  poetry run black .
  if ! test -f ".env"; then
    echo "DATABASE_URL=postgresql+psycopg2://postgres:cantguessthis@127.0.0.1/platform" >> .env
    echo "Local .env file created."
  fi
else
  poetry run black --check .
fi

poetry run pytest --cov=src --cov-fail-under=96 --no-cov-on-fail tests
poetry run coverage html --directory reports/coverage/
