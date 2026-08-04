from sqlalchemy.orm import Session

from app.modules.notes.models import Note
from app.modules.notes.schemas import (
    NoteCreate,
    NoteUpdate,
)


class NoteRepository:
    """
    Repository for customer notes.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        customer_id: str,
        author_id: str | None,
        note: NoteCreate,
    ) -> Note:
        db_note = Note(
            customer_id=customer_id,
            author_id=author_id,
            content=note.content,
        )

        self.db.add(db_note)
        self.db.flush()
        self.db.refresh(db_note)

        return db_note

    def get_customer_notes(
        self,
        customer_id: str,
    ) -> list[Note]:
        return (
            self.db.query(Note)
            .filter(Note.customer_id == customer_id)
            .order_by(Note.created_at.desc())
            .all()
        )

    def get_by_id(
        self,
        note_id: str,
    ) -> Note | None:
        return self.db.query(Note).filter(Note.id == note_id).first()

    def update(
        self,
        note: Note,
        data: NoteUpdate,
    ) -> Note:
        note.content = data.content

        self.db.flush()
        self.db.refresh(note)

        return note

    def delete(
        self,
        note: Note,
    ) -> None:
        self.db.delete(note)
        self.db.flush()
