import uuid

import pytest


@pytest.fixture
def customer_payload():
    """
    Return a valid customer payload.
    """

    return {
        "first_name": "Test",
        "last_name": "Customer",
        "email": f"customer-{uuid.uuid4()}@example.com",
        "phone": "03001234567",
    }