from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterRequest(BaseModel):
    """
    User registration request.
    """

    email: EmailStr

    username: str = Field(
        min_length=3,
        max_length=50,
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )

    first_name: str = Field(
        min_length=1,
        max_length=100,
    )

    last_name: str = Field(
        min_length=1,
        max_length=100,
    )


class RegisterResponse(BaseModel):
    """
    User registration response.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    is_active: bool
    is_superuser: bool
