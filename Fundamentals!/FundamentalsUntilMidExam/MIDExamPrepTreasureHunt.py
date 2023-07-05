initial_loot = [x for x in input().split("|")]

while True:
    command = input()

    if command == "Yohoho!":
        break
    action = command.split()
    if action[0] == "Loot":
        items = action[1:]
        for i in items:
            if i not in initial_loot:
                initial_loot.insert(0, i)
    if action[0] == "Drop":
        index = int(action[1])
        if index > len(initial_loot):
            continue
        else:
            a = initial_loot.pop(index)
            initial_loot.append(a)
    if action[0] == "Steal":
        count = int(action[1])
        stolen_items = initial_loot[-count::]
        if count <= len(initial_loot):
            print(", ".join(stolen_items))
        for it in stolen_items:
            if it in initial_loot:
                initial_loot.remove(it)

if not initial_loot:
    print("Failed treasure hunt.")
else:
    avg = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {avg:.2f} pirate credits.")
