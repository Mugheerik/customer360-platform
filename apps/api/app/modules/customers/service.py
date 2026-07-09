from sqlalchemy.orm import Session

from app.modules.customers.models import Customer
from app.modules.customers.repository import CustomerRepository
from app.modules.customers.schema import CustomerCreate


class CustomerService:
    """
    Handles customer business logic.
    """

    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)

    def create_customer(
        self,
        customer: CustomerCreate,
    ) -> Customer:

        return self.repository.create(customer)

    def get_customers(self) -> list[Customer]:

        return self.repository.get_all()