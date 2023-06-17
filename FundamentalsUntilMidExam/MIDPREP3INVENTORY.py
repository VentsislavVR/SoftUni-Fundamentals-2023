def collecting(data, some_item):
    if some_item not in data:
        data.append(some_item)
    return data


def dropping(data, some_item):
    if some_item in data:
        data.remove(some_item)
    return data


def combining(data, first, second):
    if first in data:
        index = data.index(first)
        data.insert(index + 1, second)


def renewing(data, some_item):
    if some_item in data:
        index = data.index(some_item)
        change_to_last_position = data.pop(index)
        data.append(change_to_last_position)


journal = input().split(", ")

while True:
    action = input().split(" - ")
    if action[0] == "Craft!":
        print(", ".join(journal))
        break
    elif action[0] == "Collect":
        item = action[1]
        result = collecting(journal, item)

    elif action[0] == "Drop":
        item = action[1]
        result = dropping(journal, item)

    elif action[0] == "Combine Items":
        first_second = action[1].split(":")
        first = first_second[0]
        second = first_second[1]
        result = combining(journal, first, second)

    elif action[0] == "Renew":
        item = action[1]
        result = renewing(journal,item)

