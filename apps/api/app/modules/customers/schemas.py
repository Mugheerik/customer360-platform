from datetime import datetime

from app.modules.customers.enums import CustomerStatus
from pydantic import BaseModel, ConfigDict, EmailStr


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None


class CustomerUpdate(BaseModel):
    """
    Partial customer update.

    Every field is optional so only the supplied
    values are updated.
    """

    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    status: CustomerStatus | None = None


class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None
    status: CustomerStatus
    created_at: datetime
    updated_at: datetime
