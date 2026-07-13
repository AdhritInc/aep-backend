from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "email": "prithvi@example.com",
            "password": "password123",
            "full_name": "Prithvi",
        },
    )

    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"


def test_register_duplicate_user():
    client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "password123",
            "full_name": "Duplicate User",
        },
    )

    response = client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "password123",
            "full_name": "Duplicate User",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"


def test_login_success():
    client.post(
        "/auth/register",
        json={
            "email": "login@example.com",
            "password": "password123",
            "full_name": "Login User",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "login@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_login_invalid_password():
    client.post(
        "/auth/register",
        json={
            "email": "wrongpass@example.com",
            "password": "password123",
            "full_name": "Wrong Password",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "wrongpass@example.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_login_invalid_user():
    response = client.post(
        "/auth/login",
        data={
            "username": "nouser@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"
