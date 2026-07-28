# ruff: noqa: F403
import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from tests.fixtures.users import *
from tests.fixtures.customers import *
from tests.fixtures.auth import *
from app.database.database import engine
from app.database.dependencies import get_db
from app.main import app


@pytest.fixture
def db_session():
    """
    Create a database session wrapped in a transaction.
    Each test is rolled back after execution.
    """

    connection = engine.connect()
    transaction = connection.begin()

    session = Session(bind=connection)
    session.begin_nested()

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture
def client(db_session):
    """
    Test client using the transactional database session.
    """

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def register_user(client):
    """
    Register a new user and return (user, payload).
    """

    def _register(**overrides):
        unique = uuid.uuid4().hex[:8]

        payload = {
            "email": f"user-{unique}@example.com",
            "username": f"user_{unique}",
            "password": "Password123!",
            "first_name": "John",
            "last_name": "Doe",
        }

        payload.update(overrides)

        response = client.post(
            "/api/v1/auth/register",
            json=payload,
        )

        assert response.status_code == 201

        return response.json(), payload

    return _register


@pytest.fixture
def login_user(client):
    """
    Login helper that returns an access token.
    """

    def _login(email: str, password: str):
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": email,
                "password": password,
            },
        )

        assert response.status_code == 200

        return response.json()["access_token"]

    return _login


@pytest.fixture
def user_token(register_user, login_user):
    """
    Create a user and return a valid JWT.
    """

    _, payload = register_user()

    token = login_user(
        payload["email"],
        payload["password"],
    )

    return token


@pytest.fixture
def authenticated_client(client, user_token):
    """
    Test client with Authorization header already attached.
    """

    client.headers.update(
        {
            "Authorization": f"Bearer {user_token}",
        }
    )

    return client
