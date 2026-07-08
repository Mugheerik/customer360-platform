from fastapi import APIRouter

from app.modules.customers.service import CustomerService

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

customer_service = CustomerService()


@router.get(
    "",
    summary="List customers"
)
def list_customers():

    return customer_service.get_all_customers()