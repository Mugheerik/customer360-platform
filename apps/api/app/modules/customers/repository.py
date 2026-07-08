class CustomerRepository:

    def get_all(self):

        return [
            {
                "id": 1,
                "first_name": "Ali",
                "last_name": "Khan",
                "email": "ali@example.com"
            },
            {
                "id": 2,
                "first_name": "Sara",
                "last_name": "Ahmed",
                "email": "sara@example.com"
            }
        ]