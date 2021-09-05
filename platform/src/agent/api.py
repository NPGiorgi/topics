from enum import IntEnum
from typing import List

from fastapi import APIRouter, HTTPException, status

from src import services
from src.marshal import CreateAgentPayload, AgentResponse


api = APIRouter(prefix="/agents")


@api.get("")
def get_agents_api() -> List[AgentResponse]:
    return services.get_agents()


@api.post("", status_code=status.HTTP_201_CREATED)
def create_agent_api(agent: CreateAgentPayload) -> AgentResponse:
    return services.create_agent(agent)


@api.get("/hello")
def say_hello_api():
    return {"Hello": "World"}


@api.get("/{agent_id}")
def get_agent_api(agent_id: int) -> AgentResponse:
    agent = services.get_agent(agent_id)
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found"
        )
    return agent
