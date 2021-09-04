from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists, drop_database
from starlette.testclient import TestClient

from src import settings
from src.main import app


def run_migrations():
    base_dir = Path(__file__).parent.parent
    alembic_cfg = Config(str(base_dir / "alembic.ini"))
    alembic_cfg.set_main_option("sqlalchemy.url", settings.DB_CONNECTION_URL)
    alembic_cfg.set_main_option("script_location", str(base_dir / "alembic"))
    command.upgrade(alembic_cfg, "head")


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def db():
    assert not database_exists(settings.DB_CONNECTION_URL)
    create_database(settings.DB_CONNECTION_URL)
    run_migrations()

    engine = create_engine(settings.DB_CONNECTION_URL)
    with Session(engine) as session:
        yield session

    drop_database(settings.DB_CONNECTION_URL)
