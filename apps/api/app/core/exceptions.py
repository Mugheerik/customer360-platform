class CustomerNotFoundError(Exception):
    """
    Raised when a customer cannot be found.
    """

    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self.message = f"Customer '{customer_id}' was not found."
        super().__init__(self.message)
