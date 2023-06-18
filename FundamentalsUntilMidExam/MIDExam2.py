def black_func(initial_li, som_name):
    blacklisted_name = []
    if som_name not in initial_li:
        print(f"{som_name} was not found.")
    else:
        index = initial_li.index(som_name)
        change_name = initial_li.pop(index)
        blacklisted_name.append(change_name)
        initial_li.insert(index, "blacklisted")
        print(f"{change_name} was blacklisted.")

    return initial_li


def err_func(initial_li, some_idx):
    if 0 <= some_idx < len(initial_li):
        if initial_li[some_idx] != "blacklisted" or initial_li[idx] !="Lost":
            los = initial_li.pop(some_idx)
            initial_li.insert(some_idx, los)
            print(f"{los} was lost due to an error.")
    return initial_li


def change_func(initial_li, some_idx, some_name, ):
    pass


initial_friends_list = input().split(", ")
command = input()
blaklisted = []
lost = []
while command != "Report":
    action = command.split()
    if action[0] == "Blacklist":
        name = action[1]
        initial_friends_list = black_func(initial_friends_list, name)
    elif action[0] == "Error":
        idx = int(action[1])
        initial_friends_list = err_func(initial_friends_list, idx)
    elif action[0] == "Change":
        idx = action[1]
        name = action[2]
        initial_friends_list = change_func(initial_friends_list, idx, name)

    command = input()


