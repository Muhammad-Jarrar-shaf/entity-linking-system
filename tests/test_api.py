from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200


def test_link_endpoint():
    response = client.post(
        "/link",
        json={
            "text": "Elon Musk visited Pakistan."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "entities" in data