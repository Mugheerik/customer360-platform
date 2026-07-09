from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.modules.customers.models import Customer
from app.modules.customers.repository import CustomerRepository
from app.modules.customers.schema import CustomerCreate, CustomerUpdate


class CustomerService:
    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)

    def create_customer(self, customer: CustomerCreate) -> Customer:
        return self.repository.create(customer)

    def get_customers(self) -> list[Customer]:
        return self.repository.get_all()

    def get_customer(self, customer_id: str) -> Customer:
        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found.",
            )

        return customer

    def update_customer(
        self,
        customer_id: str,
        data: CustomerUpdate,
    ) -> Customer:
        customer = self.get_customer(customer_id)

        return self.repository.update(customer, data)

    def deactivate_customer(
        self,
        customer_id: str,
    ) -> Customer:
        customer = self.get_customer(customer_id)

        return self.repository.deactivate(customer)