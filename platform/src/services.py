from typing import List, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src import settings
from src.models import Agent
from src.marshal import CreateAgentPayload, AgentResponse


def create_db_connection():
    engine = create_engine(settings.DATABASE_URL)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return scoped_session(session)


def create_agent(agent: CreateAgentPayload) -> AgentResponse:
    db = create_db_connection()
    agent = Agent(**agent.dict())
    db.add(agent)
    db.commit()
    return AgentResponse.from_orm(agent)


def get_agents() -> List[AgentResponse]:
    db = create_db_connection()
    db_agents = db.query(Agent).all()
    return [AgentResponse.from_orm(agent) for agent in db_agents]


def get_agent(agent_id: int) -> Optional[AgentResponse]:
    db = create_db_connection()
    db_agent = db.query(Agent).filter(Agent.id == agent_id).one_or_none()
    if not db_agent:
        return None
    return AgentResponse.from_orm(db_agent)
