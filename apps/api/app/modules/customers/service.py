from app.modules.customers.repository import CustomerRepository


class CustomerService:

    def __init__(self):
        self.repository = CustomerRepository()

    def get_all_customers(self):

        customers = self.repository.get_all()

        return {
            "customers": customers,
            "total": len(customers)
        }