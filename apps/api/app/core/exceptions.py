class CustomerNotFoundError(Exception):
    """
    Raised when a customer cannot be found.
    """

    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self.message = f"Customer '{customer_id}' was not found."
        super().__init__(self.message)


class ConflictError(Exception):
    """
    Raised when a requested operation conflicts with existing data.
    """

    def __init__(self, message: str):
        super().__init__(message)


class UnauthorizedError(Exception):
    """
    Raised when authentication fails.
    """

    def __init__(self, message: str = "Invalid credentials."):
        super().__init__(message)


class ForbiddenError(Exception):
    """
    Raised when a user lacks permission to perform an action.
    """

    def __init__(self, message: str = "Access denied."):
        super().__init__(message)
