from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.customers.schema import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate,
)
from app.modules.customers.service import CustomerService

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
) -> CustomerResponse:
    service = CustomerService(db)
    return CustomerResponse.model_validate(
        service.create_customer(customer)
    )


@router.get(
    "",
    response_model=list[CustomerResponse],
)
def get_customers(
    db: Session = Depends(get_db),
) -> list[CustomerResponse]:
    service = CustomerService(db)

    return [
        CustomerResponse.model_validate(customer)
        for customer in service.get_customers()
    ]


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(
    customer_id: str,
    db: Session = Depends(get_db),
) -> CustomerResponse:
    service = CustomerService(db)

    return CustomerResponse.model_validate(
        service.get_customer(customer_id)
    )


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def update_customer(
    customer_id: str,
    customer: CustomerUpdate,
    db: Session = Depends(get_db),
) -> CustomerResponse:
    service = CustomerService(db)

    updated_customer = service.update_customer(
        customer_id,
        customer,
    )

    return CustomerResponse.model_validate(updated_customer)


@router.delete(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def deactivate_customer(
    customer_id: str,
    db: Session = Depends(get_db),
) -> CustomerResponse:
    service = CustomerService(db)

    customer = service.deactivate_customer(customer_id)

    return CustomerResponse.model_validate(customer)