import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user(monkeypatch):
    class DummyUser:
        def __init__(self):
            self.id = 1
            self.first_name = "John"
            self.last_name = "Doe"
            self.email = "john@example.com"

    def fake_create_user(user):
        return DummyUser()

    monkeypatch.setattr("app.crud.create_user", fake_create_user)

    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "password": "secret",
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["first_name"] == "John"


def test_read_users(monkeypatch):
    class DummyUser:
        def __init__(self, uid):
            self.id = uid
            self.first_name = f"First{uid}"
            self.last_name = f"Last{uid}"
            self.email = f"user{uid}@example.com"

    def fake_get_users():
        return [DummyUser(1), DummyUser(2)]

    monkeypatch.setattr("app.crud.get_users", fake_get_users)

    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == 1


def test_delete_user_success(monkeypatch):
    def fake_delete_user(user_id: int):
        return True

    monkeypatch.setattr("app.crud.delete_user", fake_delete_user)

    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "User deleted"}


def test_delete_user_not_found(monkeypatch):
    def fake_delete_user(user_id: int):
        return False

    monkeypatch.setattr("app.crud.delete_user", fake_delete_user)

    response = client.delete("/users/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
