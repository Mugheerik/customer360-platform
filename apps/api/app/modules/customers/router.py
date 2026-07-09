from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.customers.schema import CustomerCreate, CustomerResponse
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

    created_customer = service.create_customer(customer)

    return CustomerResponse.model_validate(created_customer)


@router.get(
    "",
    response_model=list[CustomerResponse],
)
def get_customers(
    db: Session = Depends(get_db),
) -> list[CustomerResponse]:

    service = CustomerService(db)

    customers = service.get_customers()

    return [
        CustomerResponse.model_validate(customer)
        for customer in customers
    ]