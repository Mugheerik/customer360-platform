import logging

from sqlalchemy.orm import Session

from app.core.exceptions import (
    CustomerNotFoundError,
    NoteNotFoundError,
)
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
        customer = self.customers.get_by_id(
            customer_id,
        )

        if customer is None:
            raise CustomerNotFoundError(
                customer_id,
            )

        logger.info(
            "Creating note for customer '%s'",
            customer_id,
        )

        created_note = self.notes.create(
            customer_id=customer_id,
            author_id=author_id,
            note=note,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=customer_id,
                action=ActivityAction.UPDATED,
                actor_id=author_id,
                details={
                    "event": "note_created",
                    "note_id": created_note.id,
                },
            )
        )

        self.uow.commit()
        self.uow.refresh(created_note)

        logger.info(
            "Note '%s' created for customer '%s'",
            created_note.id,
            customer_id,
        )

        return created_note

    def get_customer_notes(
        self,
        customer_id: str,
    ) -> list[Note]:
        customer = self.customers.get_by_id(
            customer_id,
        )

        if customer is None:
            raise CustomerNotFoundError(
                customer_id,
            )

        logger.info(
            "Fetching notes for customer '%s'",
            customer_id,
        )

        return self.notes.get_customer_notes(
            customer_id,
        )

    def update_note(
        self,
        customer_id: str,
        note_id: str,
        data: NoteUpdate,
        current_user_id: str | None = None,
    ) -> Note:
        customer = self.customers.get_by_id(
            customer_id,
        )

        if customer is None:
            raise CustomerNotFoundError(
                customer_id,
            )

        note = self.notes.get_customer_note(
            customer_id=customer_id,
            note_id=note_id,
        )

        if note is None:
            raise NoteNotFoundError(
                note_id,
            )

        logger.info(
            "Updating note '%s' for customer '%s'",
            note_id,
            customer_id,
        )

        # At the current stage of Customer360 there is no
        # multi-user ownership/permission model for notes.
        #
        # Any authenticated active user may update a customer's note.
        updated_note = self.notes.update(
            note,
            data,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=customer_id,
                action=ActivityAction.UPDATED,
                actor_id=current_user_id,
                details={
                    "event": "note_updated",
                    "note_id": note_id,
                },
            )
        )

        self.uow.commit()
        self.uow.refresh(updated_note)

        logger.info(
            "Note '%s' updated successfully",
            note_id,
        )

        return updated_note

    def delete_note(
        self,
        customer_id: str,
        note_id: str,
        current_user_id: str | None = None,
    ) -> None:
        customer = self.customers.get_by_id(
            customer_id,
        )

        if customer is None:
            raise CustomerNotFoundError(
                customer_id,
            )

        note = self.notes.get_customer_note(
            customer_id=customer_id,
            note_id=note_id,
        )

        if note is None:
            raise NoteNotFoundError(
                note_id,
            )

        logger.info(
            "Deleting note '%s' from customer '%s'",
            note_id,
            customer_id,
        )

        # There is currently no note ownership/permission
        # restriction because Customer360 has not implemented
        # multi-user authorization for notes yet.
        self.notes.delete(note)

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=customer_id,
                action=ActivityAction.UPDATED,
                actor_id=current_user_id,
                details={
                    "event": "note_deleted",
                    "note_id": note_id,
                },
            )
        )

        self.uow.commit()

        logger.info(
            "Note '%s' deleted successfully",
            note_id,
        )
