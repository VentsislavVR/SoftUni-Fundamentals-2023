def data_storage(n):
    plants = {}
    for p in range(n):
        plant,rarity = input().split("<->")
        plants[plant] = {"rarity":int(rarity),"ratings":[]}
    return plants




def plant_discovery(n):
    plants = data_storage(n)

    while True:
        command = input().split("-")

        if command[0] == "Exhibition":
            print(f"Plants for the exhibition:")
            for key,value in plants.items():
                avg = sum(plants[key]['ratings']) / len(plants[key]['ratings']) if len(plants[key]['ratings']) > 0 else 0
                print(f"- {key}; Rarity: {plants[key]['rarity']}; Rating: {avg:.2f}")
            break
        action = command[0].split()

        if action[0] == "Rate:":
            plant = action[1]
            if plant in plants.keys():
                plants[plant]["ratings"].append(int(command[1]))
            else:
                print("error")

        elif action[0] == "Update:":
            plant = action[1]
            if plant in plants.keys():
                plants[plant]["rarity"] = int(command[1])
            else:
                print("error")
        elif action[0] == "Reset:":
            plant = action[1]
            if plant in plants.keys():
                plants[plant]["ratings"].clear()
            else:
                print("error")

n = int(input())
plant_discovery(n)