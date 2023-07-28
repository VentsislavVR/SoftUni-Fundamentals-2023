def plunder(cities, city, population, gold):
    cities[city]["population"] -= population
    cities[city]["gold"] -= gold
    print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")

    if 0 >= cities[city]["population"] or 0 >= cities[city]["gold"]:
        print(f"{city} has been wiped off the map!")
        del cities[city]


def prosper(cities, city, gold):
    if gold >= 0:
        cities[city]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    else:
        print("Gold added cannot be a negative number!")


def get_info(data):
    target_cities = {}
    while True:
        data = data.split("||")
        if data[0] == "Sail":
            return target_cities
        city, population, gold = data[0], int(data[1]), int(data[2])
        if city not in target_cities:
            target_cities[city] = {"population": 0, "gold": 0}
        target_cities[city]["population"] += population
        target_cities[city]["gold"] += gold
        data = input()


target_cities = get_info(input())

while True:

    command = input().split("=>")
    if command[0] == "End":
        if target_cities:
            print(f"Ahoy, Captain! There are {len(target_cities)} wealthy settlements to go to:")
            for town, stats in target_cities.items():
                print(f"{town} -> Population: {stats['population']} citizens, Gold: {stats['gold']} kg")

        else:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")
        break

    elif command[0] == "Plunder":
        attacked_city, killed_people, stolen_gold = command[1], int(command[2]), int(command[3])
        plunder(target_cities, attacked_city, killed_people, stolen_gold)
    elif command[0] == "Prosper":
        town, gold = command[1], int(command[2])
        prosper(target_cities, town, gold)

    # command = input().split("=>")
    # if command[0] == "End":
    #     break
