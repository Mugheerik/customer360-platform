import uuid


def create_customer_payload():
    email = f"test-{uuid.uuid4()}@example.com"

    return {
        "first_name": "Test",
        "last_name": "Customer",
        "email": email,
        "phone": "03001234567",
    }


def test_create_customer(client):
    payload = create_customer_payload()

    response = client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert response.status_code == 201

    data = response.json()

    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["email"] == payload["email"]


def test_get_customers(client):
    payload = create_customer_payload()

    create_response = client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    response = client.get(
        "/api/v1/customers"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_customer_by_id(client):
    payload = create_customer_payload()

    create_response = client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    response = client.get(
        f"/api/v1/customers/{customer_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id
    assert data["email"] == payload["email"]


def test_update_customer(client):
    payload = create_customer_payload()

    create_response = client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    update_payload = {
        "first_name": "Updated",
        "last_name": "Customer",
        "email": payload["email"],
        "phone": "03111111111",
        "status": "active",
    }

    response = client.put(
        f"/api/v1/customers/{customer_id}",
        json=update_payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id
    assert data["first_name"] == "Updated"
    assert data["phone"] == "03111111111"


def test_deactivate_customer(client):
    payload = create_customer_payload()

    create_response = client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    response = client.delete(
        f"/api/v1/customers/{customer_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id
    assert data["status"] == "inactive"