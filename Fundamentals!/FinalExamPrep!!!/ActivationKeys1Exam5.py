def contains_func(raw, string):
    if string in raw_keys:
        return f"{raw} contains {string}"
    else:
        return f"Substring not found!"



def flipper_func(raw_keys, command, start, end):
    if command == "Upper":
        raw_keys = raw_keys[:start_idx] + raw_keys[start_idx:end_idx].upper() + raw_keys[end_idx:]
    elif command == "Lower":
        raw_keys = raw_keys[:start_idx] + raw_keys[start_idx:end_idx].lower() + raw_keys[end_idx:]
    return raw_keys


def slice_func(raw, start_idx, end_idx):
    raw = raw[:start_idx] + raw[end_idx:]
    return raw



raw_keys = input()
result = ""
while True:
    data = input()
    if data == "Generate":
        print(f"Your activation key is: {raw_keys}")
        break
    commands = data.split(">>>")

    if commands[0] == "Contains":
        substring = commands[1]
        print(contains_func(raw_keys, substring))

    elif commands[0] == "Flip":
        upper_lower = commands[1]
        start_idx = int(commands[2])
        end_idx = int(commands[3])
        raw_keys = flipper_func(raw_keys, upper_lower, start_idx, end_idx)
        print(raw_keys)
    elif commands[0] == "Slice":
        start_idx = int(commands[1])
        end_idx = int(commands[2])
        raw_keys= slice_func(raw_keys, start_idx, end_idx)
        print(raw_keys)
