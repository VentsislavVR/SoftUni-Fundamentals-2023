from typing import List
from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []  # [Pokemon("pikachu",100),Pokemon(...,...) etc]

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"
        # return f"Caught {pokemon.name} with health{pokemon.health}"

    def release_pokemon(self, pokemon_name: str) -> str:

        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"
        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

        # try: # option 1 to iterate over instances
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return "Pokemon is not caught"
        #

    # self.pokemons.remove(pokemon)
    #
    # return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemons_data ='\n'.join([f" - {p.pokemon_details()}" for p in self.pokemons])

        return f"Pokemon Trainer {self.name}\n"\
               f"Pokemon count {len(self.pokemons)}\n"\
               f" {pokemons_data}"




pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
