from fastapi import APIRouter

from src import services
from src.marshal import CreateAgentPayload, CreateAgentResponse


api = APIRouter(prefix="/agent")


@api.post("")
def create_agent_api(agent: CreateAgentPayload) -> CreateAgentResponse:
    return services.create_agent(agent)


@api.get("/hello")
def say_hello():
    return {"Hello": "World"}
