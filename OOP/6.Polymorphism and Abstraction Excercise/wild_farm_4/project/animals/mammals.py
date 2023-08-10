from typing import List

from project.animals.animal import Mammal
from project.food import Meat, Fruit, Vegetable


class Mouse(Mammal):
    @property
    def food_that_eats(self) -> List:
        return [Fruit,Vegetable]

    @property
    def gained_weight(self) -> float:
        return 0.10

    def make_sound(self) -> str:
        return f"Squeak"

class Dog(Mammal):
    @property
    def food_that_eats(self) -> List:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.40


    def make_sound(self) -> str:
        return f"Woof!"
class Cat(Mammal):
    @property
    def food_that_eats(self) -> List:
        return [Meat,Vegetable]

    @property
    def gained_weight(self) -> float:
        return 0.30


    def make_sound(self) -> str:
        return f"Meow"


class Tiger(Mammal):
    @property
    def food_that_eats(self) -> List:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 1

    def make_sound(self) -> str:
        return f"ROAR!!!"
