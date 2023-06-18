initial_friends_list = input().split(", ")
command = input()
blacklisted = []
lost = []
while command != "Report":
    action = command.split()
    if action[0] == "Blacklist":
        name = action[1]
        if name not in initial_friends_list:
            print(f"{name} was not found.")
        else:
            index = initial_friends_list.index(name)
            change_name = initial_friends_list.pop(index)
            blacklisted.append(change_name)
            initial_friends_list.insert(index, "Blacklisted")
            print(f"{change_name} was blacklisted.")

    elif action[0] == "Error":
        idx = int(action[1])
        if 0 <= idx < len(initial_friends_list):
            if initial_friends_list[idx] == "Blacklisted" or initial_friends_list[idx] == "Lost":
                pass
            else:
                los = initial_friends_list.pop(idx)
                lost.append(los)

                initial_friends_list.insert(idx, "Lost")
                print(f"{los} was lost due to an error.")


    elif action[0] == "Change":
        idx = int(action[1])
        name = action[2]
        if 0 <= idx < len(initial_friends_list):
            old_name = initial_friends_list[idx]
            initial_friends_list.remove(old_name)
            initial_friends_list.insert(idx,name)
            print(f"{old_name} changed his username to {name}.")
    command = input()


print(f"Blacklisted names: { len(blacklisted)}")
print(f"Lost names: {len(lost)}")
# if len(blacklisted) > 0:
#     print(f"Blacklisted {''.join(blacklisted)}")
print(f"{' '.join(initial_friends_list)}")