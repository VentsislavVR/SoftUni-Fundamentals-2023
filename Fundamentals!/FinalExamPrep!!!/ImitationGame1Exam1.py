def move_letters_to_back(string, n):
    if n >= len(string):
        return string  # No change needed if n is greater than or equal to string length
    return string[n:] + string[:n]


def insert_func(string, idx, value):
    if idx > len(string):
        return string
    return string[:index] + value + string[index:]


def change_func(string, subs, newsubs):
    if subs in string:
        return string.replace(subs, newsubs)


result = ""
while True:
    message = input()
    if message == "Decode":
        break
    command = message.split("|")
    if command[0] == "Move":
        index = int(command[1])
        result = move_letters_to_back(result, index)

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        result = insert_func(result, index, value)

    elif command[0] == "ChangeAll":
        substring = command[1]
        new = command[2]
        result = change_func(result, substring, new)
    else:
        result += message

print(f"The decrypted message is: {result}")
