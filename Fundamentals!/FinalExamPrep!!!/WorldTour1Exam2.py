def add_func(text, idx, string):
    if 0 <=idx <= len(text):
        text = text[:idx] + string + text[idx:]
    return text


def remove_func(text, start, end):
    if 0 <= start <= end < len(text):
        text = text[:start] + text[end + 1:]
    return text


def switch_func(text, old, new):
    if old in text:
        text = text.replace(old, new)
    return text


destinations = input()
while True:
    data = input()

    if data == "Travel":
        print(f"Ready for world tour! Planned stops: {destinations}")
        break
    command = data.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        destinations = add_func(destinations, index, string)
        print(destinations)

    elif command[0] == "Remove Stop":
        start_idx = int(command[1])
        end_idx = int(command[2])
        destinations = remove_func(destinations, start_idx, end_idx)
        print(destinations)
    elif command[0] == "Switch":
        old = command[1]
        new = command[2]
        destinations = switch_func(destinations, old, new)
        print(destinations)
