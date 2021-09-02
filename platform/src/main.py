from fastapi import FastAPI

from src import settings
from src.agent.api import api as agent_api

app = FastAPI(debug=settings.DEBUG)
app.include_router(agent_api)
