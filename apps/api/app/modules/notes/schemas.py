from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class NoteCreate(BaseModel):
    """
    Schema for creating a customer note.
    """

    content: str


class NoteUpdate(BaseModel):
    """
    Schema for updating a customer note.
    """

    content: str


class NoteResponse(BaseModel):
    """
    Schema returned to API clients.
    """

    model_config = ConfigDict(from_attributes=True)

    id: str
    customer_id: str
    author_id: UUID | None
    content: str
    created_at: datetime
    updated_at: datetime
