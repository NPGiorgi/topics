FROM python:3.8

# create nonsudo user
RUN useradd --create-home --shell /bin/bash app

# install poetry
RUN pip3 install poetry

# set user and move to it's home dir
USER app
WORKDIR /home/app

# copy project files
COPY --chown=myapp ./src ./src
COPY --chown=myapp alembic .
COPY --chown=myapp alembic.ini .
COPY --chown=myapp poetry.lock .
COPY --chown=myapp pyproject.toml .
COPY --chown=myapp gunicorn.conf.py .

# install dependencies
RUN poetry install

# set environment
ENV PYTHONPATH=/home/app

# execute project
CMD poetry run gunicorn src.main:app
