from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_say_hello():
    response = client.get("/agent/hello")
    assert response.status_code is 200
    assert response.json() == {"Hello": "World"}
