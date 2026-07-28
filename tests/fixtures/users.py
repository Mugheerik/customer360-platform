import uuid

import pytest


@pytest.fixture
def register_payload():
    """
    Return a valid registration payload.
    """

    return {
        "email": f"user-{uuid.uuid4()}@example.com",
        "username": f"user_{uuid.uuid4().hex[:8]}",
        "password": "Password123!",
        "first_name": "John",
        "last_name": "Doe",
    }
