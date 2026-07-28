import uuid


def test_list_users_as_superuser(admin_client):
    response = admin_client.get("/api/v1/users")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1


def test_list_users_as_regular_user(authenticated_client):
    response = authenticated_client.get("/api/v1/users")

    assert response.status_code == 403

    data = response.json()

    assert data["error"]["code"] == "FORBIDDEN"
    assert data["error"]["message"] == "Insufficient permissions."


def test_get_user_by_id(admin_client, superuser):
    user_id = superuser["user"].id

    response = admin_client.get(
        f"/api/v1/users/{user_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == str(user_id)
    assert data["email"] == superuser["payload"]["email"]


def test_get_user_not_found(admin_client):
    random_id = uuid.uuid4()

    response = admin_client.get(
        f"/api/v1/users/{random_id}"
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "USER_NOT_FOUND"