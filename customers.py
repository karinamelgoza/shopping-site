"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: ${self.first_name} ${self.last_name}, ${self.email}'


def read_customers():

    customers = {}

    file = open('customers.txt')
    for line in file:
        first_name, last_name, email, password = line.strip().split('|')
        customers[email] = Customer(first_name, last_name, email, password)

    return customers


def get_by_email(email):

    return customers[email]


customers = read_customers()
