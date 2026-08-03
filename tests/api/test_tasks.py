# tests/api/test_tasks.py

import uuid


def create_customer_payload():
    email = f"task-{uuid.uuid4()}@example.com"

    return {
        "first_name": "Task",
        "last_name": "Customer",
        "email": email,
        "phone": "03001234567",
    }


def create_task_payload():
    return {
        "title": "Follow up with customer",
        "description": "Call customer tomorrow",
        "priority": "medium",
        "assigned_to": None,
    }


def create_customer(client):
    response = client.post(
        "/api/v1/customers",
        json=create_customer_payload(),
    )

    assert response.status_code == 201

    return response.json()


def create_task(
    client,
    customer_id: str,
):
    response = client.post(
        f"/api/v1/customers/{customer_id}/tasks",
        json=create_task_payload(),
    )

    assert response.status_code == 201

    return response.json()


def test_create_task(client):
    customer = create_customer(client)

    response = client.post(
        f"/api/v1/customers/{customer['id']}/tasks",
        json=create_task_payload(),
    )

    assert response.status_code == 201

    data = response.json()

    assert data["customer_id"] == customer["id"]
    assert data["title"] == "Follow up with customer"
    assert data["description"] == "Call customer tomorrow"
    assert data["priority"] == "medium"
    assert data["status"] == "todo"


def test_get_customer_tasks(client):
    customer = create_customer(client)

    create_task(
        client,
        customer["id"],
    )

    response = client.get(
        f"/api/v1/customers/{customer['id']}/tasks",
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1

    assert data[0]["customer_id"] == customer["id"]
    assert data[0]["title"] == "Follow up with customer"


def test_update_task(client):
    customer = create_customer(client)

    task = create_task(
        client,
        customer["id"],
    )

    response = client.patch(
        f"/api/v1/customers/{customer['id']}/tasks/{task['id']}",
        json={
            "title": "Updated task",
            "description": "Updated description",
            "priority": "high",
            "status": "done",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task["id"]
    assert data["customer_id"] == customer["id"]
    assert data["title"] == "Updated task"
    assert data["description"] == "Updated description"
    assert data["priority"] == "high"
    assert data["status"] == "done"


def test_delete_task(client):
    customer = create_customer(client)

    task = create_task(
        client,
        customer["id"],
    )

    response = client.delete(
        f"/api/v1/customers/{customer['id']}/tasks/{task['id']}",
    )

    assert response.status_code == 204

    response = client.get(
        f"/api/v1/customers/{customer['id']}/tasks",
    )

    assert response.status_code == 200
    assert response.json() == []


def test_create_task_customer_not_found(client):
    response = client.post(
        f"/api/v1/customers/{uuid.uuid4()}/tasks",
        json=create_task_payload(),
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "CUSTOMER_NOT_FOUND"


def test_get_customer_tasks_customer_not_found(client):
    response = client.get(
        f"/api/v1/customers/{uuid.uuid4()}/tasks",
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "CUSTOMER_NOT_FOUND"


def test_update_task_not_found(client):
    customer = create_customer(client)

    response = client.patch(
        f"/api/v1/customers/{customer['id']}/tasks/{uuid.uuid4()}",
        json={
            "title": "Updated",
        },
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "TASK_NOT_FOUND"


def test_delete_task_not_found(client):
    customer = create_customer(client)

    response = client.delete(
        f"/api/v1/customers/{customer['id']}/tasks/{uuid.uuid4()}",
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "TASK_NOT_FOUND"
