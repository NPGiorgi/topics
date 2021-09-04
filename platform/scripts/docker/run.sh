#!/bin/bash

# runs the container using local db
docker run -p 8000:8000 -e PORT=8000 -e DB_CONNECTION_URL=postgresql+psycopg2://postgres:cantguessthis@127.0.0.1/platform --name platform -d platform:local
