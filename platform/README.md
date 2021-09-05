# Platform Microservice

## Prerequisites

* [Python 3.8+](https://www.python.org/downloads/release/python-3810/).
* [Poetry](https://python-poetry.org/docs/#installation)
* [Docker](https://docs.docker.com/engine/install/)
* [Postgres](#install-postgres-database)

## Install

Run the following command:

```shell
$ sh build.sh
```

## Run locally

```shell
$ sh ./scripts/run-local.sh
```

## Run tests

```shell
$ sh ./scripts/run-tests.sh
```

## Run migrations

```shell
$ sh ./scripts/migrate.sh
```

## To add a dependency

```shell
$ poetry add dependency-name
```

To make it dev only pass the `-D` flag:

```shell
$ poetry add -D dependency-name
```

# Install Postgres Database

To run Postgres we will use Docker, so make sure it's installed.
Run the following commands in order to have Postgres running on you system
for local development.

1 - Pull latest postgres image

```shell
$ docker pull postgres
```

2 - Create the docker container

__Note: Replace {pass} with the desired password, for this project, **FOR LOCAL DEVELOPMENT ONLY**, we will be using the password 'cantguesthis'.__

```shell
docker run --name postgres -e POSTGRES_PASSWORD={pass} -d -p 5432:5432 postgres
```

You can stop the container using `docker stop postgres` and start it using `docker start postgres`. 
