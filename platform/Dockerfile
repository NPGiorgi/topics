# pull base python image
FROM python:3.8

# install poetry
RUN pip3 install poetry

# copy project files
COPY ./src ./src
COPY alembic .
COPY alembic.ini .
COPY poetry.lock .
COPY pyproject.toml .
COPY gunicorn.conf.py .

# install dependencies
RUN poetry install

# set environment
ENV PYTHONPATH=/home/app

# execute project
CMD poetry run gunicorn src.main:app
