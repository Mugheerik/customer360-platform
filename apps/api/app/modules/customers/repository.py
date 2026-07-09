from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.customers.models import Customer
from app.modules.customers.schema import CustomerCreate, CustomerUpdate


class CustomerRepository:
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
        statement = (
            select(Customer)
            .where(Customer.status == "active")
            .order_by(Customer.created_at.desc())
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(self, customer_id: str) -> Customer | None:
        statement = (
            select(Customer)
            .where(Customer.id == customer_id)
        )

        return self.db.scalar(statement)

    def update(
        self,
        customer: Customer,
        data: CustomerUpdate,
    ) -> Customer:
        customer.first_name = data.first_name
        customer.last_name = data.last_name
        customer.email = data.email
        customer.phone = data.phone
        customer.status = data.status

        self.db.commit()
        self.db.refresh(customer)

        return customer

    def deactivate(
        self,
        customer: Customer,
    ) -> Customer:
        customer.status = "inactive"

        self.db.commit()
        self.db.refresh(customer)

        return customer