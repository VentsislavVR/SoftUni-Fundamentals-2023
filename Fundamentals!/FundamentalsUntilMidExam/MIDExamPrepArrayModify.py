def swap_func(first, second, data):
    data[first], data[second] = data[second], data[first]
    return data


def multiply_func(first, second, data):
    data[first] = int(data[first]) * int(data[second])
    return data


def decrease_func(data):
    data = [int(x) - 1 for x in data]
    return data


def modifier_func(data):
    while True:
        command = input()
        if command == "end":
            print(", ".join([str(num) for num in data]))
            break
        command = command.split(" ")
        current_command = command[0]
        if current_command == "swap":
            first = int(command[1])
            second = int(command[2])
            data = swap_func(first, second, data)
        elif current_command == "multiply":
            first = int(command[1])
            second = int(command[2])
            data = multiply_func(first, second, data)
        elif current_command == "decrease":
            data = decrease_func(data)
    return data


data = input().split(" ")
modifier_func(data)

