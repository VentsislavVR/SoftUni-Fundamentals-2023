from typing import List
from customer import Customer
from dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if dvd in customer.rented_dvds:
            return (f"{customer.name}"
                    f" has already rented {dvd.name}")

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self)->str:
        customers = [c for c in self.customers]
        dvd = [d for d in self.dvds]
        res = ''
        for c in self.customers:
            res += f"{c}\n"
        for dvd in self.dvds:
            res += f'{dvd}\n'

        return res
