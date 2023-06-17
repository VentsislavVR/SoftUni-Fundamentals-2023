pokemons = [ int(x) for x in input().split()]

total_sum_pokemons = 0
while pokemons:
    current_pokemon = int(input())
    if current_pokemon == len(pokemons):
        pokemons[-1] = pokemons[0]
    else:
        catch = pokemons.pop(current_pokemon)
        total_sum_pokemons += catch
    catch2 = catch

    for index, c in enumerate(pokemons):
        if c <= current_pokemon:
            pokemons[index] += catch
            current_pokemon +=catch
        else:
            pokemons[index] -= catch
            current_pokemon +=catch

print(total_sum_pokemons)