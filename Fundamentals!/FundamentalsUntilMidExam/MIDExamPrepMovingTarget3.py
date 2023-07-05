def shoot(list_of_targets, target_index, shoot_power):
    if target_index in range(len(list_of_targets)):
        if list_of_targets[target_index] <= shoot_power:
            list_of_targets.pop(target_index)
        else:
            list_of_targets[target_index] -= shoot_power
        return list_of_targets


def add(list_of_targets, target_index, target_value):
    if target_index in range(len(list_of_targets)):
        list_of_targets.insert(target_index, value)
    else:
        print("Invalid placement!")
    return list_of_targets


def strike(list_of_targets, target_index, radius):
    if target_index - radius in range(len(list_of_targets)) and \
            target_index + radius in range(len(list_of_targets)):
        list_of_targets = list_of_targets[0:target_index - radius] +\
                          list_of_targets[target_index + radius + 1:]
    else:  # some of edge indexes is not valid
        print("Strike missed!")
    return list_of_targets


targets = [int(target) for target in input().split()]
command = input()
while command != "End":
    command = command.split()
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)
    command = input()
print(*targets, sep="|")