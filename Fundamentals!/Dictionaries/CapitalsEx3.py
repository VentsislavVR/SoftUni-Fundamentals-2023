countries = input().split(", ")
capitals = input().split(", ")

# capital_by_country = {countries[idx]: capitals[idx] for idx in range(len(countries))} # dict comprehension
capital_by_country = [f"{countries[idx]} -> {capitals[idx]}" for idx in range(len(countries))] # list comprehension

print("\n".join(capital_by_country))