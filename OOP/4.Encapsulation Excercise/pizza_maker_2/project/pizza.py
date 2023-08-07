from typing import Dict

from dough import Dough
from topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int) -> None:
        self.name = name
        self.dough: Dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str:, float] = {}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value == "":
            raise ValueError("The name cannot bean empty string")
        self.__name = value

    @property
    def dough(self) -> Dough:
        return self.__dough

    @dough.setter
    def dough(self, value: Dough):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self) -> int:
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int) -> None:
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> None:
        if self.__max_number_of_toppings <= len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self) -> float:
        return sum(self.toppings.values()) + self.dough.weight
