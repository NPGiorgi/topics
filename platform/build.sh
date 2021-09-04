#!/bin/bash

poetry install
poetry run black .
poetry run pytest --cov=src --cov-fail-under=96 --no-cov-on-fail --cov-branch tests
poetry run coverage html --directory reports/coverage/
