import pytest
from fastapi.testclient import TestClient
from app.main import app
import dotenv, os, time

dotenv.load_dotenv()

client = TestClient(app)


def test_root():
    '''
    Teste le status de la requête
    '''
    response = client.get("/")
    assert response.status_code == 200


def test_get_user():
    '''
    Teste le status de la requête et le résultat attendu
    '''
    user = {"name": "John Doe", "email": "test@test.fr", "id": 100}
    response = client.post(url="/user/100", json=user)
    assert response.status_code == 200
    assert response.json() == user
