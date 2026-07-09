from sqlalchemy.orm import Session

from app.modules.customers.repository import CustomerRepository
from app.modules.customers.schema import CustomerCreate
from app.modules.customers.models import Customer


class CustomerService:
    """
    Handles customer business logic.
    """

    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)

    def create_customer(self, customer: CustomerCreate) -> Customer:
        """
        Create a new customer.
        """

        return self.repository.create(customer)