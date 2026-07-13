from app.auth.identity import (
    create_access_token,
    hash_password,
    verify_access_token,
    verify_password,
)


def test_hash_password():
    password = "password123"

    hashed_password = hash_password(password)

    assert hashed_password != password


def test_verify_password_success():
    password = "password123"

    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password)


def test_verify_password_failure():
    password = "password123"

    hashed_password = hash_password(password)

    assert not verify_password("wrongpassword", hashed_password)


def test_create_access_token():
    token = create_access_token(
        data={"sub": "prithvi@example.com"},
    )

    assert token is not None
    assert isinstance(token, str)


def test_verify_access_token():
    token = create_access_token(
        data={"sub": "prithvi@example.com"},
    )

    payload = verify_access_token(token)

    assert payload["sub"] == "prithvi@example.com"


def test_verify_invalid_token():
    payload = verify_access_token("invalid-token")

    assert payload is None