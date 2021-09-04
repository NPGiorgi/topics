from src.models import Agent

# noinspection PyUnresolvedReferences
from tests.fixtures import db, client



def test_say_hello(client):
    response = client.get("/agent/hello")
    assert response.status_code is 200
    assert response.json() == {"Hello": "World"}


def test_create_agent_api(client, db):
    payload = {"name": "Test", "secretName": "Secret"}

    response = client.post("/agent", json=payload)

    agents = db.query(Agent).all()
    assert len(agents) == 1
    agent = agents[0]
    assert isinstance(agent.id, int)
    assert agent.name == "Test"
    assert agent.secret_name == "Secret"

    result = response.json()
    assert isinstance(result["id"], int)
    assert result["name"] == "Test"
    assert result["secretName"] == "Secret"



