import pytest
import uuid

@pytest.fixture
def registered_user(client, register_payload):
    """
    Register a user and return the response payload.
    """

    response = client.post(
        "/api/v1/auth/register",
        json=register_payload,
    )

    assert response.status_code == 201

    return {
        "payload": register_payload,
        "user": response.json(),
    }


@pytest.fixture
def access_token(client, registered_user):
    """
    Log in and return an access token.
    """

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": registered_user["payload"]["email"],
            "password": registered_user["payload"]["password"],
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]


@pytest.fixture
def authenticated_client(client, access_token):
    """
    TestClient with Authorization header.
    """

    client.headers.update(
        {
            "Authorization": f"Bearer {access_token}",
        }
    )

    return client


@pytest.fixture
def superuser_payload():
    return {
        "email": f"admin-{uuid.uuid4()}@example.com",
        "username": f"admin_{uuid.uuid4().hex[:8]}",
        "password": "Password123!",
        "first_name": "Admin",
        "last_name": "User",
    }


@pytest.fixture
def superuser(client, db_session, superuser_payload):
    response = client.post(
        "/api/v1/auth/register",
        json=superuser_payload,
    )

    assert response.status_code == 201

    from app.modules.users.models import User

    user = (
        db_session.query(User)
        .filter(User.email == superuser_payload["email"])
        .first()
    )

    user.is_superuser = True

    db_session.commit()

    return {
        "payload": superuser_payload,
        "user": user,
    }


@pytest.fixture
def admin_client(client, superuser):
    login = client.post(
        "/api/v1/auth/login",
        json={
            "email": superuser["payload"]["email"],
            "password": superuser["payload"]["password"],
        },
    )

    token = login.json()["access_token"]

    client.headers.update(
        {
            "Authorization": f"Bearer {token}",
        }
    )

    return client