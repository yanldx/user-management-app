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
            self.firstname = "John"
            self.lastname = "Doe"
            self.email = "john@example.com"
            self.birthdate = "1990-01-01"
            self.city = "Paris"
            self.postal_code = "75000"
            self.is_admin = False

    def fake_create_user(user, db=None):
        return DummyUser()

    monkeypatch.setattr("app.routers.users.create_user", fake_create_user)

    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "email": "john@example.com",
        "password": "secret",
        "birthdate": "1990-01-01",
        "city": "Paris",
        "postal_code": "75000"
    }
    response = client.post("/api/users", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "John"
    assert data["lastname"] == "Doe"
    assert data["email"] == "john@example.com"


def test_read_users(monkeypatch):
    class DummyUser:
        def __init__(self, uid):
            self.id = uid
            self.firstname = f"First{uid}"
            self.lastname = f"Last{uid}"
            self.email = f"user{uid}@example.com"
            self.birthdate = "1990-01-01"
            self.city = "Paris"
            self.postal_code = "75000"
            self.is_admin = False

    def fake_list_users(db=None):
        return [DummyUser(1), DummyUser(2)]

    monkeypatch.setattr("app.routers.users.list_users", fake_list_users)

    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == 1


def test_delete_user_success(monkeypatch):
    def fake_delete_user(id: int, db=None, admin=None):
        return {"message": "Utilisateur supprimé"}

    monkeypatch.setattr("app.routers.users.delete_user", fake_delete_user)

    response = client.delete("/api/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Utilisateur supprimé"}


def test_delete_user_not_found(monkeypatch):
    from fastapi import HTTPException

    def fake_delete_user(id: int, db=None, admin=None):
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    monkeypatch.setattr("app.routers.users.delete_user", fake_delete_user)

    response = client.delete("/api/users/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Utilisateur introuvable"
    