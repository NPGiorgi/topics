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

# poetry install everything globally
RUN poetry config virtualenvs.create false

# install dependencies
RUN poetry install

# execute project
CMD gunicorn src.main:app
