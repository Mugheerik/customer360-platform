# ruff: noqa: F403

import uuid

from tests.fixtures.auth import *
from tests.fixtures.customers import *
from tests.fixtures.users import *


def create_customer_payload():
    email = f"note-test-{uuid.uuid4()}@example.com"

    return {
        "first_name": "Note",
        "last_name": "Customer",
        "email": email,
        "phone": "03001234567",
    }


def create_customer(client):
    response = client.post(
        "/api/v1/customers",
        json=create_customer_payload(),
    )

    assert response.status_code == 201

    return response.json()


def create_note(
    authenticated_client,
    customer_id,
):
    response = authenticated_client.post(
        f"/api/v1/customers/{customer_id}/notes",
        json={
            "content": "Initial customer note.",
        },
    )

    assert response.status_code == 201

    return response.json()


def test_create_note(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    customer_id = customer["id"]

    response = authenticated_client.post(
        f"/api/v1/customers/{customer_id}/notes",
        json={
            "content": "Initial customer note.",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["customer_id"] == customer_id
    assert data["content"] == "Initial customer note."
    assert data["author_id"] is not None
    assert data["id"]
    assert data["created_at"]
    assert data["updated_at"]


def test_get_customer_notes(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    customer_id = customer["id"]

    create_note(
        authenticated_client,
        customer_id,
    )

    response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}/notes",
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["customer_id"] == customer_id
    assert data[0]["content"] == "Initial customer note."


def test_update_note(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    customer_id = customer["id"]

    note = create_note(
        authenticated_client,
        customer_id,
    )

    note_id = note["id"]

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer_id}/notes/{note_id}",
        json={
            "content": "Updated customer note.",
        },
    )

    print("\nUPDATE STATUS:", response.status_code)
    print("UPDATE RESPONSE:", response.text)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == note_id
    assert data["customer_id"] == customer_id
    assert data["content"] == "Updated customer note."


def test_delete_note(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    customer_id = customer["id"]

    note = create_note(
        authenticated_client,
        customer_id,
    )

    note_id = note["id"]

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer_id}/notes/{note_id}",
    )

    print("\nDELETE STATUS:", response.status_code)
    print("DELETE RESPONSE:", response.text)

    assert response.status_code == 204
    assert response.content == b""

    get_response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}/notes",
    )

    assert get_response.status_code == 200
    assert get_response.json() == []


def test_create_note_for_missing_customer(
    authenticated_client,
):
    customer_id = str(uuid.uuid4())

    response = authenticated_client.post(
        f"/api/v1/customers/{customer_id}/notes",
        json={
            "content": "This should fail.",
        },
    )

    assert response.status_code == 404


def test_get_notes_for_missing_customer(
    authenticated_client,
):
    customer_id = str(uuid.uuid4())

    response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}/notes",
    )

    assert response.status_code == 404


def test_update_missing_note(
    authenticated_client,
):
    customer = create_customer(
        authenticated_client,
    )

    customer_id = customer["id"]
    note_id = str(uuid.uuid4())

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer_id}/notes/{note_id}",
        json={
            "content": "This should fail.",
        },
    )

    assert response.status_code == 404


def test_delete_missing_note(
    authenticated_client,
):
    customer = create_customer(
        authenticated_client,
    )

    customer_id = customer["id"]
    note_id = str(uuid.uuid4())

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer_id}/notes/{note_id}",
    )

    assert response.status_code == 404


def test_note_cannot_be_accessed_through_another_customer(
    authenticated_client,
):
    first_customer = create_customer(
        authenticated_client,
    )

    second_customer = create_customer(
        authenticated_client,
    )

    first_customer_id = first_customer["id"]
    second_customer_id = second_customer["id"]

    note = create_note(
        authenticated_client,
        first_customer_id,
    )

    note_id = note["id"]

    update_response = authenticated_client.patch(
        f"/api/v1/customers/{second_customer_id}/notes/{note_id}",
        json={
            "content": "This should not be allowed.",
        },
    )

    assert update_response.status_code == 404

    delete_response = authenticated_client.delete(
        f"/api/v1/customers/{second_customer_id}/notes/{note_id}",
    )

    assert delete_response.status_code == 404

    original_response = authenticated_client.get(
        f"/api/v1/customers/{first_customer_id}/notes",
    )

    assert original_response.status_code == 200

    data = original_response.json()

    assert len(data) == 1
    assert data[0]["id"] == note_id
    assert data[0]["content"] == "Initial customer note."
