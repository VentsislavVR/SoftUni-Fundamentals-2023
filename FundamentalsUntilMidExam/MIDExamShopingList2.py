def urgent_func(shopping_li, item):
    if item not in shopping_li:
        shopping_li.insert(0,item)
    return shopping_li


def unnecessary_func(shopping_li, item):
    if item in shopping_li:
        shopping_li.remove(item)
    return shopping_li


def correct_func(shopping_li, old_item, new_item):
    if old_item in shopping_li:
        index = shopping_li.index(old_item)
        shopping_li[index] = new_item
    return shopping_li


def rearrange_func(shopping_li, item):
    if item in shopping_li:
        shopping_li.remove(item)
        shopping_li.append(item)
    return shopping_li


shopping_list = [x for x in input().split("!")]
command = input()
while command != "Go Shopping!":
    action = command.split()
    if action[0] == "Urgent":
        item = action[1]
        shopping_list = urgent_func(shopping_list, item)
    elif action[0] == "Unnecessary":
        item = action[1]
        shopping_list = unnecessary_func(shopping_list, item)
    elif action[0] == "Correct":
        old_item = action[1]
        new_item = action[2]
        shopping_list = correct_func(shopping_list, old_item, new_item)
    elif action[0] == "Rearrange":
        item = action[1]
        shopping_list = rearrange_func(shopping_list, item)

    command = input()
print(*shopping_list, sep=", ")