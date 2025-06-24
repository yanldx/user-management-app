import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Reset DB before each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_user():
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


def test_read_users():
    # Create a user first
    client.post("/api/users", json={
        "firstname": "Alice",
        "lastname": "Smith",
        "email": "alice@example.com",
        "password": "secret",
        "birthdate": "1991-01-01",
        "city": "Lyon",
        "postal_code": "69000"
    })

    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert "firstname" in data[0]


def test_delete_user_success():
    # Create a user first
    res = client.post("/api/users", json={
        "firstname": "User",
        "lastname": "ToDelete",
        "email": "delete@example.com",
        "password": "secret",
        "birthdate": "1990-01-01",
        "city": "Paris",
        "postal_code": "75000"
    })
    user_id = res.json()["id"]

    # Simulate admin login
    os.environ["ADMIN_EMAIL"] = "admin@test.com"
    os.environ["ADMIN_PASSWORD"] = "adminpass"
    client.app.router.on_startup[0]()  # Trigger create_admin

    login_res = client.post("/api/login", json={
        "email": "admin@test.com",
        "password": "adminpass"
    })
    token = login_res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete(f"/api/users/{user_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Utilisateur supprimé"


def test_delete_user_not_found():
    os.environ["ADMIN_EMAIL"] = "admin@test.com"
    os.environ["ADMIN_PASSWORD"] = "adminpass"
    client.app.router.on_startup[0]()  # Trigger create_admin

    login_res = client.post("/api/login", json={
        "email": "admin@test.com",
        "password": "adminpass"
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.delete("/api/users/9999", headers=headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Utilisateur introuvable"
    