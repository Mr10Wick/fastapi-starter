from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_create_and_get_user():
    payload = {"name": "Ada Lovelace", "email": "ada@example.com"}
    r = client.post("/users", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "Ada Lovelace"
    assert data["email"] == "ada@example.com"

    # Récupération
    r2 = client.get(f"/users/{payload['email']}")
    assert r2.status_code == 200
    assert r2.json()["email"] == payload["email"]
