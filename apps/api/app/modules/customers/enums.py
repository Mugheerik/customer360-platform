from enum import StrEnum


class CustomerStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class CustomerSortField(StrEnum):
    CREATED_AT = "created_at"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    EMAIL = "email"


class SortOrder(StrEnum):
    ASC = "asc"
    DESC = "desc"
