def plunder_func(city_dict, city_name, city_population, city_gold):
    city_is_valid = True
    if city_name in city_dict.keys():
        city_dict[city_name][0] -= city_population
        city_dict[city_name][1] -= city_gold
        if city_dict[city_name][0] <= 0 or city_dict[city_name][1] <= 0:
            city_dict.pop(city_name)
            city_is_valid = False
            return f"{city_name} plundered! {city_gold} gold stolen, {city_population} citizens killed."'\n'f"{city_name} has been wiped off the map!"
        return f"{city_name} plundered! {city_gold} gold stolen, {city_population} citizens killed."


def prosper_func(city_dict, city_name, city_gold):
    if city_name in city_dict:
        if city_gold < 0:
            return "Gold added cannot be a negative number!"
        city_dict[city_name][1] += city_gold
    return f"{city_gold} gold added to the city treasury. {city_name} now has {city_dict[city_name][1]} gold."


city_dict = {}
while True:
    line = input()
    if line == "Sail":
        break
    target_cities = line.split("||")
    city = target_cities[0]
    population = int(target_cities[1])
    gold = int(target_cities[2])
    if city not in city_dict.keys():
        city_dict[city] = [population, gold]
    else:
        city_dict[city][0] += population
        city_dict[city][1] += gold

while True:
    data = input()
    if data == "End":
        break
    events = data.split("=>")
    if events[0] == "Plunder":
        city = events[1]
        people = int(events[2])
        gold = int(events[3])
        result = print(plunder_func(city_dict, city, people, gold))

    elif events[0] == "Prosper":
        city = events[1]
        gold = int(events[2])
        result = print(prosper_func(city_dict, city, gold))
if city_dict:
    print(f"Ahoy, Captain! There are {len(city_dict)} wealthy settlements to go to:")
    for town, value in city_dict.items():
        print(f"{town} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
