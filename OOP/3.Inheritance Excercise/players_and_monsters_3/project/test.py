from hero import Hero
from elf import Elf
from blade_knight import BladeKnight


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
blade = BladeKnight("Killer",99)
print(blade.__class__.__bases__[0].__name__)
