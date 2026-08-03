import logging

from sqlalchemy.orm import Session

from app.core.exceptions import CustomerNotFoundError
from app.core.uow import UnitOfWork
from app.modules.activity.enums import (
    ActivityAction,
    EntityType,
)
from app.modules.activity.schemas import ActivityCreate
from app.modules.notes.models import Note
from app.modules.notes.schemas import (
    NoteCreate,
    NoteUpdate,
)

logger = logging.getLogger(__name__)


class NoteService:
    """
    Business logic for customer notes.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.uow = UnitOfWork(db)

        self.notes = self.uow.notes
        self.customers = self.uow.customers
        self.activities = self.uow.activities

    def create_note(
        self,
        customer_id: str,
        author_id: str | None,
        note: NoteCreate,
    ) -> Note:
        customer = self.customers.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundError(customer_id)

        logger.info(
            "Creating note for customer '%s'",
            customer_id,
        )

        created_note = self.notes.create(
            customer_id,
            author_id,
            note,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=customer_id,
                action=ActivityAction.UPDATED,
                performed_by=author_id,
                details={
                    "event": "note_created",
                },
            )
        )

        self.uow.commit()
        self.uow.refresh(created_note)

        return created_note

    def get_customer_notes(
        self,
        customer_id: str,
    ) -> list[Note]:
        customer = self.customers.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundError(customer_id)

        return self.notes.get_customer_notes(customer_id)

    def update_note(
        self,
        note_id: str,
        data: NoteUpdate,
    ) -> Note:
        note = self.notes.get_by_id(note_id)

        if note is None:
            raise ValueError("Note not found.")

        updated_note = self.notes.update(
            note,
            data,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=note.customer_id,
                action=ActivityAction.UPDATED,
                details={
                    "event": "note_updated",
                },
            )
        )

        self.uow.commit()
        self.uow.refresh(updated_note)

        return updated_note

    def delete_note(
        self,
        note_id: str,
    ) -> None:
        note = self.notes.get_by_id(note_id)

        if note is None:
            raise ValueError("Note not found.")

        customer_id = note.customer_id

        self.notes.delete(note)

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=customer_id,
                action=ActivityAction.UPDATED,
                details={
                    "event": "note_deleted",
                },
            )
        )

        self.uow.commit()
