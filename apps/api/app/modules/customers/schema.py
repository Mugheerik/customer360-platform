from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    """
    Schema used when creating a new customer.

    This represents data that the API accepts from external clients.
    """

    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None


class CustomerResponse(BaseModel):
    """
    Schema used when returning customer information.

    This represents data exposed by the API.
    """

    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    created_at: datetime