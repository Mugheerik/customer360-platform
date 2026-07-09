import logging

from sqlalchemy.orm import Session

from app.modules.customers.repository import CustomerRepository
from app.modules.customers.schemas import (
    CustomerCreate,
    CustomerResponse,
)

logger = logging.getLogger(__name__)


class CustomerService:
    """
    Business logic for customer operations.
    """

    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)

    def create_customer(
        self,
        customer: CustomerCreate,
    ) -> CustomerResponse:
        logger.info(
            "Creating customer with email '%s'",
            customer.email,
        )

        created_customer = self.repository.create(customer)

        logger.info(
            "Customer '%s' created successfully",
            created_customer.id,
        )

        return CustomerResponse.model_validate(created_customer)

    def list_active_customers(self) -> list[CustomerResponse]:
        logger.info("Fetching active customers")

        customers = self.repository.get_active_customers()

        logger.info(
            "Retrieved %s active customers",
            len(customers),
        )

        return [
            CustomerResponse.model_validate(customer)
            for customer in customers
        ]