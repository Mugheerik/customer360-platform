from app.database.dependencies import get_db
from app.modules.activity.schemas import ActivityResponse
from app.modules.customers.queries import CustomerQueryParams
from app.modules.customers.schemas import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate,
)
from app.modules.customers.service import CustomerService
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


def get_customer_service(
    db: Session = Depends(get_db),
) -> CustomerService:
    return CustomerService(db)


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_customer(
    customer: CustomerCreate,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    return CustomerResponse.model_validate(service.create_customer(customer))


@router.get(
    "",
    response_model=list[CustomerResponse],
)
def get_customers(
    query: CustomerQueryParams = Depends(),
    service: CustomerService = Depends(get_customer_service),
) -> list[CustomerResponse]:
    return [
        CustomerResponse.model_validate(customer)
        for customer in service.get_customers(query)
    ]


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(
    customer_id: str,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    return CustomerResponse.model_validate(service.get_customer(customer_id))


@router.get(
    "/{customer_id}/timeline",
    response_model=list[ActivityResponse],
)
def get_customer_timeline(
    customer_id: str,
    service: CustomerService = Depends(get_customer_service),
) -> list[ActivityResponse]:
    timeline = service.get_customer_timeline(
        customer_id,
    )

    return [ActivityResponse.model_validate(activity) for activity in timeline]


@router.patch(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def update_customer(
    customer_id: str,
    customer: CustomerUpdate,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    updated_customer = service.update_customer(
        customer_id,
        customer,
    )

    return CustomerResponse.model_validate(
        updated_customer,
    )


@router.delete(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def deactivate_customer(
    customer_id: str,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    customer = service.deactivate_customer(
        customer_id,
    )

    return CustomerResponse.model_validate(customer)
