def test_login_success(client, registered_user):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": registered_user["payload"]["email"],
            "password": registered_user["payload"]["password"],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client, registered_user):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": registered_user["payload"]["email"],
            "password": "WrongPassword123!",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["error"]["code"] == "UNAUTHORIZED"
    assert data["error"]["message"] == "Invalid email or password."


def test_login_unknown_email(client):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "Password123!",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["error"]["code"] == "UNAUTHORIZED"
    assert data["error"]["message"] == "Invalid email or password."
