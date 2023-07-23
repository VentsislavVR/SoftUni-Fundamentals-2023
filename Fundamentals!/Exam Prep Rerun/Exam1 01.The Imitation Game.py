secret_message = input()

while True:
    command = input().split("|")

    if command[0] == "Decode":
        print(f"The decrypted message is: {secret_message}")
        break
    elif command[0] == "Move":
        first_letters = int(command[1])
        secret_message = secret_message[first_letters:] + secret_message[:first_letters]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        secret_message = secret_message[:index] + value + secret_message[index:]
    elif command[0] == "ChangeAll":
        substring = command[1]
        new = command[2]
        secret_message = secret_message.replace(substring, new)
