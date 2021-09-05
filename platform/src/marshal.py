from typing import Optional

from pydantic import BaseModel


def to_camel_case(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


class Model(BaseModel):
    class Config:
        alias_generator = to_camel_case


class RequestModel(Model):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ResponseModel(RequestModel):
    pass


class CreateAgentPayload(RequestModel):
    id: Optional[str]
    name: str
    secret_name: str


class AgentResponse(ResponseModel):
    id: int
    name: str
    secret_name: str
