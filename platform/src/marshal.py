from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


def to_camel_case(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


def isoformat(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")  # i.e. 2020-10-19T09:01:48-05:00


class Model(BaseModel):
    class Config:
        alias_generator = to_camel_case
        json_encoders = {UUID: str, datetime: isoformat, Enum: lambda enum: enum.value}


class ResponseModel(Model):
    pass


class RequestModel(Model):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CreateAgentPayload(RequestModel):
    id: Optional[str]
    name: str
    secret_name: str


class CreateAgentResponse(RequestModel):
    id: str
    name: str
    secret_name: str
