import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import (
    ConflictError,
    CustomerNotFoundError,
)
from app.core.uow import UnitOfWork
from app.modules.activity.enums import (
    ActivityAction,
    EntityType,
)
from app.modules.activity.models import ActivityLog
from app.modules.activity.schemas import ActivityCreate
from app.modules.customers.models import Customer
from app.modules.customers.queries import CustomerQueryParams
from app.modules.customers.schemas import (
    CustomerCreate,
    CustomerUpdate,
)

logger = logging.getLogger(__name__)


class CustomerService:
    """
    Business logic for customer operations.

    Transaction ownership belongs to the service layer through
    the UnitOfWork. A single business operation should normally
    result in a single database commit.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.uow = UnitOfWork(db)

        self.customers = self.uow.customers
        self.activities = self.uow.activities

    def create_customer(
        self,
        customer: CustomerCreate,
        actor_id: str,
    ) -> Customer:
        logger.info(
            "Creating customer with email '%s'",
            customer.email,
        )

        try:
            created_customer = self.customers.create(
                customer,
            )

            self.uow.flush()

            self.activities.create(
                ActivityCreate(
                    entity_type=EntityType.CUSTOMER,
                    entity_id=str(created_customer.id),
                    action=ActivityAction.CREATED,
                    actor_id=actor_id,
                )
            )

            self.uow.commit()
            self.uow.refresh(created_customer)

        except IntegrityError as err:
            self.uow.rollback()

            raise ConflictError(
                f"Customer with email '{customer.email}' already exists."
            ) from err

        except Exception:
            self.uow.rollback()

            logger.exception(
                "Failed to create customer '%s'. Transaction rolled back.",
                customer.email,
            )

            raise

        logger.info(
            "Customer '%s' created successfully",
            created_customer.id,
        )

        return created_customer

    def get_customers(
        self,
        query: CustomerQueryParams,
    ):
        """
        Retrieve a paginated list of customers.
        """

        logger.info(
            "Fetching customers - page=%d size=%d",
            query.page,
            query.size,
        )

        result = self.customers.get_all(
            query,
        )

        logger.info(
            "Retrieved %d customers out of %d",
            len(result.items),
            result.total,
        )

        return result

    def get_customer(
        self,
        customer_id: str,
    ) -> Customer:
        logger.info(
            "Fetching customer '%s'",
            customer_id,
        )

        customer = self.customers.get_by_id(
            customer_id,
        )

        if customer is None:
            logger.warning(
                "Customer '%s' not found",
                customer_id,
            )

            raise CustomerNotFoundError(
                customer_id,
            )

        return customer

    def update_customer(
        self,
        customer_id: str,
        data: CustomerUpdate,
        actor_id: str,
    ) -> Customer:
        customer = self.get_customer(
            customer_id,
        )

        logger.info(
            "Updating customer '%s'",
            customer_id,
        )

        updated_customer = self.customers.update(
            customer,
            data,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=str(
                    updated_customer.id,
                ),
                action=ActivityAction.UPDATED,
                actor_id=actor_id,
            )
        )

        try:
            self.uow.commit()

        except Exception:
            self.uow.rollback()

            logger.exception(
                "Failed to update customer '%s'",
                customer_id,
            )

            raise

        self.uow.refresh(
            updated_customer,
        )

        logger.info(
            "Customer '%s' updated successfully",
            customer_id,
        )

        return updated_customer

    def activate_customer(
        self,
        customer_id: str,
        actor_id: str,
    ) -> Customer:
        customer = self.get_customer(
            customer_id,
        )

        logger.info(
            "Activating customer '%s'",
            customer_id,
        )

        updated_customer = self.customers.activate(
            customer,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=str(
                    updated_customer.id,
                ),
                action=ActivityAction.ACTIVATED,
                actor_id=actor_id,
            )
        )

        try:
            self.uow.commit()

        except Exception:
            self.uow.rollback()

            logger.exception(
                "Failed to activate customer '%s'",
                customer_id,
            )

            raise

        self.uow.refresh(
            updated_customer,
        )

        logger.info(
            "Customer '%s' activated",
            customer_id,
        )

        return updated_customer

    def deactivate_customer(
        self,
        customer_id: str,
        actor_id: str,
    ) -> Customer:
        customer = self.get_customer(
            customer_id,
        )

        logger.info(
            "Deactivating customer '%s'",
            customer_id,
        )

        updated_customer = self.customers.deactivate(
            customer,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=str(
                    updated_customer.id,
                ),
                action=ActivityAction.DEACTIVATED,
                actor_id=actor_id,
            )
        )

        try:
            self.uow.commit()

        except Exception:
            self.uow.rollback()

            logger.exception(
                "Failed to deactivate customer '%s'",
                customer_id,
            )

            raise

        self.uow.refresh(
            updated_customer,
        )

        logger.info(
            "Customer '%s' deactivated",
            customer_id,
        )

        return updated_customer

    def get_customer_timeline(
        self,
        customer_id: str,
    ) -> list[ActivityLog]:
        """
        Retrieve the activity timeline for a customer.
        """

        self.get_customer(
            customer_id,
        )

        logger.info(
            "Fetching timeline for customer '%s'",
            customer_id,
        )

        return self.activities.get_customer_timeline(
            customer_id,
        )
