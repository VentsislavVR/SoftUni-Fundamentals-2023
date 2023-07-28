def flip(keys,up_low,start,end):
    if up_low == "Upper":
        keys =  raw_keys[:start] + raw_keys[start:end].upper() + raw_keys[end:]
        return keys

    elif up_low == "Lower":
        keys = raw_keys[:start] + raw_keys[start:end].lower() + raw_keys[end:]
        return keys




raw_keys = input()

while True:
    command = input().split(">>>")

    if command[0] == "Generate":
        print(f"Your activation key is: {raw_keys}")
        break

    elif command[0] =="Contains":
        substring = command[1]

        if substring in raw_keys:
            print(f"{raw_keys} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command[0] == "Flip":
        up_low = command[1]
        start_idx = int(command[2])
        end_idx = int(command[3])
        raw_keys = flip(raw_keys,up_low,start_idx,end_idx)
        print(raw_keys)

        pass
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_keys = raw_keys[:start_index] + raw_keys[end_index:]
        print(raw_keys)
