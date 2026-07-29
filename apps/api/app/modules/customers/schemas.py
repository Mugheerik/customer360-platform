from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.modules.customers.enums import CustomerStatus


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None


class CustomerUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    status: CustomerStatus


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