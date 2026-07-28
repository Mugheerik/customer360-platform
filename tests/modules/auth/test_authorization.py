def test_me_with_token(authenticated_client):
    response = authenticated_client.get(
        "/api/v1/auth/me",
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "email" in data
    assert "username" in data
    assert data["is_active"] is True


def test_me_without_token(client):
    response = client.get(
        "/api/v1/auth/me",
    )

    assert response.status_code == 401

    data = response.json()

    assert data["error"]["code"] == "UNAUTHORIZED"
    assert data["error"]["message"] == "Not authenticated"


def test_me_invalid_token(client):
    response = client.get(
        "/api/v1/auth/me",
        headers={
            "Authorization": "Bearer invalid-token",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["error"]["code"] == "UNAUTHORIZED"
    assert data["error"]["message"] == "Invalid authentication credentials."
