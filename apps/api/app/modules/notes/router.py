from app.core.security.dependencies import get_current_user
from app.database.dependencies import get_db
from app.modules.notes.schemas import (
    NoteCreate,
    NoteResponse,
    NoteUpdate,
)
from app.modules.notes.service import NoteService
from app.modules.users.models import User
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/customers/{customer_id}/notes",
    tags=["Notes"],
)


def get_note_service(
    db: Session = Depends(get_db),
) -> NoteService:
    return NoteService(db)


@router.post(
    "",
    response_model=NoteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_note(
    customer_id: str,
    note: NoteCreate,
    current_user: User = Depends(get_current_user),
    service: NoteService = Depends(get_note_service),
) -> NoteResponse:
    created_note = service.create_note(
        customer_id=customer_id,
        author_id=str(current_user.id),
        note=note,
    )

    return NoteResponse.model_validate(created_note)


@router.get(
    "",
    response_model=list[NoteResponse],
)
def get_customer_notes(
    customer_id: str,
    service: NoteService = Depends(get_note_service),
) -> list[NoteResponse]:
    notes = service.get_customer_notes(customer_id)

    return [NoteResponse.model_validate(note) for note in notes]


@router.patch(
    "/{note_id}",
    response_model=NoteResponse,
)
def update_note(
    customer_id: str,
    note_id: str,
    note: NoteUpdate,
    service: NoteService = Depends(get_note_service),
) -> NoteResponse:
    updated_note = service.update_note(
        note_id,
        note,
    )

    return NoteResponse.model_validate(updated_note)


@router.delete(
    "/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_note(
    customer_id: str,
    note_id: str,
    service: NoteService = Depends(get_note_service),
) -> None:
    service.delete_note(note_id)
