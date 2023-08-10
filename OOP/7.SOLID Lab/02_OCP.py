class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Making sound"
class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + " holy s@it i can talk"


class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + " meaw or miaw ? meow :?"


class Chicken(Animal):
    def make_sound(self):
        return super().make_sound() + " chicken noise"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('ariel'), Dog('sharo'), Chicken('chicken')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
