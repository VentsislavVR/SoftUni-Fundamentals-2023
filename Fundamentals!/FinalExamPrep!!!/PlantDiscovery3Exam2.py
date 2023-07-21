n = int(input())
plants = {

}
for i in range(n):
    data = input().split("<->")
    plant,rarity = data[0],data[1]
    if plant not in plants:
        plants[plant]= {"rarity":int(rarity),"ratings":[]}


while True:
    command = input().split("-")

    if command[0] == "Exhibition":
        break
    action = command[0].split()
    off = action[0]
    plant = action[1]
    if plant in plants:
        if off == "Rate:":
            rating = int(command[1])
            plants[plant]["ratings"].append(rating)
        elif off == "Update:":
            rarity = int(command[1])
            plants[plant]["rarity"] = rarity
        elif off == "Reset:":
            plants[plant]["ratings"].clear()
    else:
        print("error")
print("Plants for the exhibition:")
for key,value in plants.items():
    # ratings =sum(plants[plant]['ratings'])/ len(plants[plant]['ratings'])
    if len(plants[key]["ratings"]) < 1:
        rating = 0
    else:
        rating= sum(plants[key]["ratings"]) / len(plants[key]['ratings'])
    print(f"- {key}; Rarity: {plants[key]['rarity']}; Rating: {rating:.2f}")
