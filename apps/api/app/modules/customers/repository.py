from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.customers.models import Customer
from app.modules.customers.schema import CustomerCreate


class CustomerRepository:
    """
    Handles all database operations
    related to customers.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, customer: CustomerCreate) -> Customer:

        db_customer = Customer(
            first_name=customer.first_name,
            last_name=customer.last_name,
            email=customer.email,
            phone=customer.phone,
        )

        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)

        return db_customer

    def get_all(self) -> list[Customer]:
        """
        Retrieve all customers.
        """

        statement = select(Customer)

        return list(self.db.scalars(statement).all())