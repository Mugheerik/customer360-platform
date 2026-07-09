from fastapi import APIRouter

from app.modules.customers.schema import CustomerCreate
from app.modules.customers.service import CustomerService


router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)


customer_service = CustomerService()


@router.post("")
def create_customer(
    customer: CustomerCreate
):
    """
    Create a new customer.

    Request data is validated by Pydantic
    before reaching this function.
    """

    return customer_service.create_customer(customer)