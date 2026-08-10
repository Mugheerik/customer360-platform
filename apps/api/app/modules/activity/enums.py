from enum import StrEnum


class ActivityAction(StrEnum):
    """
    Supported activity actions.
    """

    CREATED = "created"
    UPDATED = "updated"
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"


class EntityType(StrEnum):
    """
    Supported platform entities.
    """

    CUSTOMER = "customer"
    USER = "user"
