import uuid


def create_customer_payload():
    email = f"test-{uuid.uuid4()}@example.com"

    return {
        "first_name": "Test",
        "last_name": "Customer",
        "email": email,
        "phone": "03001234567",
    }


def test_create_customer(authenticated_client):
    payload = create_customer_payload()

    response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert response.status_code == 201

    data = response.json()

    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["email"] == payload["email"]


def test_get_customers(authenticated_client):
    payload = create_customer_payload()

    create_response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    response = authenticated_client.get(
        "/api/v1/customers",
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert "items" in data
    assert "page" in data
    assert "size" in data
    assert "total" in data
    assert "pages" in data

    assert isinstance(data["items"], list)
    assert len(data["items"]) > 0

    assert data["page"] == 1
    assert data["size"] == 20
    assert data["total"] >= 1
    assert data["pages"] >= 1


def test_get_customer_by_id(authenticated_client):
    payload = create_customer_payload()

    create_response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id
    assert data["email"] == payload["email"]


def test_update_customer(authenticated_client):
    payload = create_customer_payload()

    create_response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    update_payload = {
        "phone": "03111111111",
    }

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer_id}",
        json=update_payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id

    assert data["phone"] == "03111111111"

    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["email"] == payload["email"]
    assert data["status"] == "active"


def test_deactivate_customer(authenticated_client):
    payload = create_customer_payload()

    create_response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer_id}",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id
    assert data["status"] == "inactive"


def test_create_customer_duplicate_email(authenticated_client):
    payload = create_customer_payload()

    response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert response.status_code == 201

    duplicate_response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert duplicate_response.status_code == 409

    data = duplicate_response.json()

    assert data["error"]["code"] == "CONFLICT"
    assert (
        data["error"]["message"]
        == f"Customer with email '{payload['email']}' already exists."
    )


def test_create_customer_creates_activity(
    authenticated_client,
):
    payload = create_customer_payload()

    response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert response.status_code == 201

    customer = response.json()

    customer_id = customer["id"]

    timeline_response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}/timeline",
    )

    assert timeline_response.status_code == 200

    timeline = timeline_response.json()

    assert len(timeline) >= 1

    created_events = [event for event in timeline if event["action"] == "created"]

    assert len(created_events) == 1

    created_event = created_events[0]

    assert created_event["entity_type"] == "customer"
    assert created_event["entity_id"] == customer_id


def test_update_customer_creates_activity(
    authenticated_client,
):
    payload = create_customer_payload()

    create_response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer_id}",
        json={
            "phone": "03111111111",
        },
    )

    assert response.status_code == 200

    timeline_response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}/timeline",
    )

    assert timeline_response.status_code == 200

    timeline = timeline_response.json()

    updated_events = [event for event in timeline if event["action"] == "updated"]

    assert len(updated_events) >= 1

    updated_event = updated_events[0]

    assert updated_event["entity_type"] == "customer"
    assert updated_event["entity_id"] == customer_id


def test_deactivate_customer_creates_activity(
    authenticated_client,
):
    payload = create_customer_payload()

    create_response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert create_response.status_code == 201

    customer = create_response.json()

    customer_id = customer["id"]

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer_id}",
    )

    assert response.status_code == 200

    timeline_response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}/timeline",
    )

    assert timeline_response.status_code == 200

    timeline = timeline_response.json()

    deactivated_events = [
        event for event in timeline if event["action"] == "deactivated"
    ]

    assert len(deactivated_events) == 1

    deactivated_event = deactivated_events[0]

    assert deactivated_event["entity_type"] == "customer"
    assert deactivated_event["entity_id"] == customer_id


def test_create_customer_rolls_back_when_activity_fails(
    authenticated_client,
    monkeypatch,
):
    payload = create_customer_payload()

    def patched_create(
        self,
        activity,
    ):
        raise RuntimeError(
            "Simulated activity creation failure",
        )

    monkeypatch.setattr(
        "app.modules.activity.repository.ActivityRepository.create",
        patched_create,
    )

    response = authenticated_client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert response.status_code == 500

    get_response = authenticated_client.get(
        "/api/v1/customers",
    )

    assert get_response.status_code == 200

    data = get_response.json()

    matching_customers = [
        customer for customer in data["items"] if customer["email"] == payload["email"]
    ]

    assert matching_customers == []
