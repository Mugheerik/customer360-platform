from enum import StrEnum


class ActivityAction(StrEnum):
    """
    Supported activity actions.
    """

    CREATED = "created"
    UPDATED = "updated"
    DEACTIVATED = "deactivated"


class EntityType(StrEnum):
    """
    Supported platform entities.
    """

    CUSTOMER = "customer"
    USER = "user"
