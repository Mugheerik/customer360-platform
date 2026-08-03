from app.core.exceptions import ConflictError
from app.modules.customers.enums import (
    CustomerStatus,
    SortOrder,
)
from app.modules.customers.models import Customer
from app.modules.customers.queries import CustomerQueryParams
from app.modules.customers.schemas import (
    CustomerCreate,
    CustomerUpdate,
)
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        customer: CustomerCreate,
    ) -> Customer:
        db_customer = Customer(
            first_name=customer.first_name,
            last_name=customer.last_name,
            email=customer.email,
            phone=customer.phone,
        )

        self.db.add(db_customer)

        return db_customer

    def get_all(
        self,
        query: CustomerQueryParams,
    ) -> list[Customer]:
        statement = select(Customer)

        if query.status is not None:
            statement = statement.where(Customer.status == query.status)

        if query.search:
            search = f"%{query.search}%"

            statement = statement.where(
                Customer.first_name.ilike(search)
                | Customer.last_name.ilike(search)
                | Customer.email.ilike(search)
            )

        sort_column = getattr(
            Customer,
            query.sort.value,
        )

        if query.order == SortOrder.DESC:
            statement = statement.order_by(sort_column.desc())
        else:
            statement = statement.order_by(sort_column.asc())

        offset = (query.page - 1) * query.size

        statement = statement.offset(offset).limit(query.size)

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        customer_id: str,
    ) -> Customer | None:
        statement = select(Customer).where(Customer.id == customer_id)

        return self.db.scalar(statement)

    def update(
        self,
        customer: Customer,
        data: CustomerUpdate,
    ) -> Customer:
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(
                customer,
                field,
                value,
            )

        return customer

    def deactivate(
        self,
        customer: Customer,
    ) -> Customer:
        customer.status = CustomerStatus.INACTIVE

        return customer

    def flush(self) -> None:
        """
        Flush pending database changes.

        Used by the service layer before commit so
        IntegrityError can still be translated into
        domain exceptions.
        """
        try:
            self.db.flush()

        except IntegrityError as err:
            self.db.rollback()

            raise ConflictError("Customer with this email already exists.") from err
