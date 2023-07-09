def rev_func(text, string):
    error_flag = False  # Flag to track error
    if string not in text:
        print("error")
        error_flag = True
        return text, error_flag
    else:
        text = text.replace(string, "",1)
        string = string[::-1]
        text += string
    return text, error_flag


hidden_message = input()

while True:
    data = input()
    if data == "Reveal":
        break
    command = data.split(":|:")

    if command[0] == "InsertSpace":
        idx = int(command[1])
        hidden_message = hidden_message[:idx] + " " + hidden_message[idx:]
        print(hidden_message)
    elif command[0] == "Reverse":
        substring = command[1]
        hidden_message,error= rev_func(hidden_message,substring)
        if not error:
            print(hidden_message)

    elif command[0] == "ChangeAll":
        old = command[1]
        new= command[2]
        hidden_message= hidden_message.replace(old,new)
        print(hidden_message)


print(f"You have a new text message: {hidden_message}")
