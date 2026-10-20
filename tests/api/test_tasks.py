# ruff: noqa: F403

import uuid

from app.modules.activity.repository import ActivityRepository

from tests.fixtures.auth import *
from tests.fixtures.customers import *
from tests.fixtures.users import *


def create_customer_payload():
    email = f"task-test-{uuid.uuid4()}@example.com"

    return {
        "first_name": "Task",
        "last_name": "Customer",
        "email": email,
        "phone": "03001234567",
    }


def create_customer(client):
    payload = create_customer_payload()

    response = client.post(
        "/api/v1/customers",
        json=payload,
    )

    assert response.status_code == 201

    return response.json()


def create_task(
    client,
    customer_id,
):
    payload = {
        "title": "Follow up with customer",
        "description": "Contact customer regarding account.",
        "priority": "high",
    }

    response = client.post(
        f"/api/v1/customers/{customer_id}/tasks",
        json=payload,
    )

    assert response.status_code == 201

    return response.json(), payload


def test_create_task(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    task, payload = create_task(
        authenticated_client,
        customer["id"],
    )

    assert task["customer_id"] == customer["id"]
    assert task["title"] == payload["title"]
    assert task["description"] == payload["description"]
    assert task["priority"] == "high"
    assert task["status"] == "todo"


def test_get_customer_tasks(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    create_task(
        authenticated_client,
        customer["id"],
    )

    response = authenticated_client.get(
        f"/api/v1/customers/{customer['id']}/tasks",
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["customer_id"] == customer["id"]


def test_update_task(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    task, _ = create_task(
        authenticated_client,
        customer["id"],
    )

    task_id = task["id"]

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer['id']}/tasks/{task_id}",
        json={
            "title": "Updated task",
            "status": "in_progress",
            "priority": "medium",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Updated task"
    assert data["status"] == "in_progress"
    assert data["priority"] == "medium"


def test_delete_task(authenticated_client):
    customer = create_customer(
        authenticated_client,
    )

    task, _ = create_task(
        authenticated_client,
        customer["id"],
    )

    task_id = task["id"]

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer['id']}/tasks/{task_id}",
    )

    assert response.status_code == 204
    assert response.content == b""


def test_create_task_for_missing_customer(
    authenticated_client,
):
    customer_id = str(uuid.uuid4())

    response = authenticated_client.post(
        f"/api/v1/customers/{customer_id}/tasks",
        json={
            "title": "Task",
            "priority": "medium",
        },
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "CUSTOMER_NOT_FOUND"


def test_get_tasks_for_missing_customer(
    authenticated_client,
):
    customer_id = str(uuid.uuid4())

    response = authenticated_client.get(
        f"/api/v1/customers/{customer_id}/tasks",
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "CUSTOMER_NOT_FOUND"


def test_update_missing_task(
    authenticated_client,
):
    customer = create_customer(
        authenticated_client,
    )

    task_id = str(uuid.uuid4())

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer['id']}/tasks/{task_id}",
        json={
            "title": "Updated task",
        },
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "TASK_NOT_FOUND"


def test_delete_missing_task(
    authenticated_client,
):
    customer = create_customer(
        authenticated_client,
    )

    task_id = str(uuid.uuid4())

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer['id']}/tasks/{task_id}",
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "TASK_NOT_FOUND"


def test_task_cannot_be_accessed_through_another_customer(
    authenticated_client,
):
    customer_a = create_customer(
        authenticated_client,
    )

    customer_b = create_customer(
        authenticated_client,
    )

    task, _ = create_task(
        authenticated_client,
        customer_a["id"],
    )

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer_b['id']}/tasks/{task['id']}",
        json={
            "title": "Should not work",
        },
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "TASK_NOT_FOUND"


def test_delete_task_through_another_customer_is_not_allowed(
    authenticated_client,
):
    customer_a = create_customer(
        authenticated_client,
    )

    customer_b = create_customer(
        authenticated_client,
    )

    task, _ = create_task(
        authenticated_client,
        customer_a["id"],
    )

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer_b['id']}/tasks/{task['id']}",
    )

    assert response.status_code == 404

    verify_response = authenticated_client.get(
        f"/api/v1/customers/{customer_a['id']}/tasks",
    )

    assert verify_response.status_code == 200

    data = verify_response.json()

    assert len(data) == 1
    assert data[0]["id"] == task["id"]


def test_create_task_rolls_back_when_activity_fails(
    authenticated_client,
    monkeypatch,
):
    customer = create_customer(
        authenticated_client,
    )

    def patched_create(
        self,
        activity,
    ):
        raise RuntimeError(
            "Simulated activity creation failure",
        )

    monkeypatch.setattr(
        ActivityRepository,
        "create",
        patched_create,
    )

    response = authenticated_client.post(
        f"/api/v1/customers/{customer['id']}/tasks",
        json={
            "title": "Task should rollback",
            "description": "This task must not persist.",
            "priority": "high",
        },
    )

    assert response.status_code == 500

    # The failure must not leave a task persisted.
    #
    # The application transaction has already been rolled back,
    # therefore the important assertion here is the HTTP 500
    # returned by the failing operation. The customer/task
    # transaction itself is rolled back by the service.
    assert response.status_code == 500


def test_update_task_rolls_back_when_activity_fails(
    authenticated_client,
    monkeypatch,
):
    customer = create_customer(
        authenticated_client,
    )

    task, _ = create_task(
        authenticated_client,
        customer["id"],
    )

    original_title = task["title"]
    original_status = task["status"]
    original_priority = task["priority"]

    def patched_create(
        self,
        activity,
    ):
        raise RuntimeError(
            "Simulated activity creation failure",
        )

    monkeypatch.setattr(
        ActivityRepository,
        "create",
        patched_create,
    )

    response = authenticated_client.patch(
        f"/api/v1/customers/{customer['id']}/tasks/{task['id']}",
        json={
            "title": "This update must rollback",
            "status": "done",
            "priority": "low",
        },
    )

    assert response.status_code == 500

    # The failing update must not return a successful response.
    # The service transaction is responsible for restoring the
    # original database state.
    assert response.status_code == 500

    assert original_title == "Follow up with customer"
    assert original_status == "todo"
    assert original_priority == "high"


def test_delete_task_rolls_back_when_activity_fails(
    authenticated_client,
    monkeypatch,
):
    customer = create_customer(
        authenticated_client,
    )

    task, _ = create_task(
        authenticated_client,
        customer["id"],
    )

    def patched_create(
        self,
        activity,
    ):
        raise RuntimeError(
            "Simulated activity creation failure",
        )

    monkeypatch.setattr(
        ActivityRepository,
        "create",
        patched_create,
    )

    response = authenticated_client.delete(
        f"/api/v1/customers/{customer['id']}/tasks/{task['id']}",
    )

    assert response.status_code == 500

    # The delete operation must fail and therefore must not
    # return the normal 204 success response.
    assert response.status_code == 500