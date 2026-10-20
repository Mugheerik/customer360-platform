# ruff: noqa: F403

import uuid

import pytest
from app.database.database import engine
from app.database.dependencies import get_db
from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import event
from sqlalchemy.orm import Session

from tests.fixtures.auth import *
from tests.fixtures.customers import *
from tests.fixtures.users import *


@pytest.fixture
def db_session():
    """
    Create a database session for tests.

    The session uses an outer transaction with a nested SAVEPOINT so
    normal application commits do not permanently persist test data.

    Application-level rollbacks are allowed to occur without leaving
    the SQLAlchemy session in a broken state.
    """

    connection = engine.connect()
    transaction = connection.begin()

    session = Session(
        bind=connection,
        expire_on_commit=False,
    )

    session.begin_nested()

    @event.listens_for(
        session,
        "after_transaction_end",
    )
    def restart_savepoint(
        session,
        transaction,
    ):
        if (
            transaction.nested
            and transaction.parent is not None
            and not transaction.parent.nested
        ):
            session.begin_nested()

    try:
        yield session

    finally:
        event.remove(
            session,
            "after_transaction_end",
            restart_savepoint,
        )

        session.close()

        if transaction.is_active:
            transaction.rollback()

        connection.close()


@pytest.fixture
def client(db_session):
    """
    Test client using the transactional database session.

    Server exceptions are converted into HTTP 500 responses instead
    of being re-raised into pytest. This allows API tests to verify
    the application's error-handling behavior.
    """

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(
        app,
        raise_server_exceptions=False,
    ) as client:
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

    def _login(
        email: str,
        password: str,
    ):
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
def user_token(
    register_user,
    login_user,
):
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
def authenticated_client(
    client,
    user_token,
):
    """
    Test client with Authorization header already attached.
    """

    client.headers.update(
        {
            "Authorization": f"Bearer {user_token}",
        }
    )

    return client