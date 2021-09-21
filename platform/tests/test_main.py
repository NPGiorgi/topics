from src.models import Agent

# noinspection PyUnresolvedReferences
from tests.fixtures import db, client


def test_say_hello(client):
    response = client.get("/agents/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "UCU"}


def test_get_agents_api(client, db):
    existing_agent = Agent(name="Name", secret_name="Secret")
    db.add(existing_agent)
    db.commit()

    response = client.get("/agents")

    assert response.json() == [
        {"id": existing_agent.id, "name": "Name", "secretName": "Secret"}
    ]


def test_get_agent_api(client, db):
    existing_agent = Agent(name="Name", secret_name="Secret")
    db.add(existing_agent)
    db.commit()

    response = client.get(f"/agents/{existing_agent.id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": existing_agent.id,
        "name": "Name",
        "secretName": "Secret",
    }


def test_get_agent_api_404(client, db):
    response = client.get(f"/agents/1")

    assert response.status_code == 404


def test_create_agent_api(client, db):
    payload = {"name": "Test", "secretName": "Secret"}

    response = client.post("/agents", json=payload)

    assert response.status_code == 201
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
