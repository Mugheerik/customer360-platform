import logging

from sqlalchemy.orm import Session

from app.core.exceptions import CustomerNotFoundError
from app.modules.customers.models import Customer
from app.modules.customers.repository import CustomerRepository
from app.modules.customers.schemas import (
    CustomerCreate,
    CustomerUpdate,
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
    ) -> Customer:
        logger.info(
            "Creating customer with email '%s'",
            customer.email,
        )

        created_customer = self.repository.create(customer)

        logger.info(
            "Customer '%s' created successfully",
            created_customer.id,
        )

        return created_customer

    def get_customers(self) -> list[Customer]:
        logger.info("Fetching active customers")

        customers = self.repository.get_all()

        logger.info(
            "Retrieved %d active customers",
            len(customers),
        )

        return customers

    def get_customer(
        self,
        customer_id: str,
    ) -> Customer:
        logger.info(
            "Fetching customer '%s'",
            customer_id,
        )

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            logger.warning(
                "Customer '%s' not found",
                customer_id,
            )
            raise CustomerNotFoundError(customer_id)

        return customer

    def update_customer(
        self,
        customer_id: str,
        data: CustomerUpdate,
    ) -> Customer:
        customer = self.get_customer(customer_id)

        logger.info(
            "Updating customer '%s'",
            customer_id,
        )

        updated_customer = self.repository.update(
            customer,
            data,
        )

        logger.info(
            "Customer '%s' updated successfully",
            customer_id,
        )

        return updated_customer

    def deactivate_customer(
        self,
        customer_id: str,
    ) -> Customer:
        customer = self.get_customer(customer_id)

        logger.info(
            "Deactivating customer '%s'",
            customer_id,
        )

        customer = self.repository.deactivate(customer)

        logger.info(
            "Customer '%s' deactivated",
            customer_id,
        )

        return customer
