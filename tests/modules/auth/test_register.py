import uuid


def test_register_success(client, register_payload):
    response = client.post(
        "/api/v1/auth/register",
        json=register_payload,
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == register_payload["email"]
    assert data["username"] == register_payload["username"]
    assert data["first_name"] == register_payload["first_name"]
    assert data["last_name"] == register_payload["last_name"]


def test_register_duplicate_email(client, register_payload):
    response = client.post(
        "/api/v1/auth/register",
        json=register_payload,
    )

    assert response.status_code == 201

    duplicate_payload = register_payload.copy()
    duplicate_payload["username"] = f"user_{uuid.uuid4().hex[:8]}"

    response = client.post(
        "/api/v1/auth/register",
        json=duplicate_payload,
    )

    assert response.status_code == 409

    data = response.json()

    assert data["error"]["code"] == "CONFLICT"
    assert data["error"]["message"] == "Email is already registered."


def test_register_duplicate_username(client, register_payload):
    response = client.post(
        "/api/v1/auth/register",
        json=register_payload,
    )

    assert response.status_code == 201

    duplicate_payload = register_payload.copy()
    duplicate_payload["email"] = f"user-{uuid.uuid4()}@example.com"

    response = client.post(
        "/api/v1/auth/register",
        json=duplicate_payload,
    )

    assert response.status_code == 409

    data = response.json()

    assert data["error"]["code"] == "CONFLICT"
    assert data["error"]["message"] == "Username is already taken."