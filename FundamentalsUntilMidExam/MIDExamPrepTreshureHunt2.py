# "Yohoho!"
# •	"Loot {item1} {item2}…{itemn}":
# •	"Drop {index}":
# •	"Steal {count}":
def loot(loots, list_of_items):
    for item in list_of_items:
        if item not in loots:
            loots.insert(0, item)
    return loots


def drop(loots, target_index):
    if target_index in range(len(loots)):#index is valid
        removed_loot = loots.pop(target_index)
        loots.append(removed_loot)
    return loots


def steal(loots,count_of_steal ):
    if count_of_steal >= len(loots):
        print(", ".join(loots))
        loots = []
    else:
        steal_index = len(loots) - count_of_steal
        print(", ".join(loots[steal_index:]))
        loots = loots[0:steal_index]
    return loots



initial_loot = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]

    if action == "Loot":
        items = command[1:]
        initial_loot = loot(initial_loot, items)
    elif action == "Drop":
        index = int(command[1])
        initial_loot = drop(initial_loot, index)
    elif action == "Steal":
        count = int(command[1])
        initial_loot = steal(initial_loot,count)
    command = input()

if not initial_loot:
    print("Failed treasure hunt.")
else:
    average_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

