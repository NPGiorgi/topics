from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src import settings
from src.models import Agent
from src.marshal import CreateAgentPayload, CreateAgentResponse


def create_db_connection():
    engine = create_engine(settings.DB_CONNECTION_URL)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return scoped_session(session)


def create_agent(agent: CreateAgentPayload) -> CreateAgentResponse:
    db = create_db_connection()
    agent = Agent(**agent.dict())
    db.add(agent)
    db.commit()
    return CreateAgentResponse.from_orm(agent)
