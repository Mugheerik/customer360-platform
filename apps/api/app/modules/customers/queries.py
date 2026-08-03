from app.modules.customers.enums import (
    CustomerSortField,
    CustomerStatus,
    SortOrder,
)
from pydantic import BaseModel, Field


class CustomerQueryParams(BaseModel):
    """
    Query parameters for listing customers.
    """

    search: str | None = None

    status: CustomerStatus | None = None

    page: int = Field(
        default=1,
        ge=1,
    )

    size: int = Field(
        default=20,
        ge=1,
        le=100,
    )

    sort: CustomerSortField = CustomerSortField.CREATED_AT

    order: SortOrder = SortOrder.DESC
