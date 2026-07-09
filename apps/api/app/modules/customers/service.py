from app.modules.customers.schema import CustomerCreate


class CustomerService:
    """
    Handles customer business logic.

    Database operations will be introduced later.
    For now, this layer demonstrates separation
    between API and business rules.
    """

    def create_customer(
        self,
        customer: CustomerCreate
    ):
        """
        Creates a customer.

        Currently returns validated input.
        Database persistence will be added
        in the database engineering phase.
        """

        return customer