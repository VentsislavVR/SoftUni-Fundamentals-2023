from abc import ABC, abstractmethod
from typing import List

from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def make_sound(self) -> str:
        ...

    @property
    @abstractmethod
    def feed(self):
        ...

    @property
    @abstractmethod
    def gain_weight(self) -> float:
        ...

    @property
    @abstractmethod
    def food_that_eats(self) -> List[Food]:
        ...


class Bird(ABC, Animal):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"[{self.name}, "
                f"{self.wing_size}, "
                f"{self.weight}, "
                f"{self.food_eaten}]")


class Mammel(ABC, Animal):
    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"[{self.name},"
                f" {self.weight},"
                f" {self.living_region},"
                f"{self.food_eaten}]")
