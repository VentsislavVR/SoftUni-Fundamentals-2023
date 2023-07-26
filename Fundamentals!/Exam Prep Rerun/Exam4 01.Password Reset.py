password = input()

while True:
    command = input()

    if command == "Done":
        print(f"Your password is: {password}")
        break
    actions = command.split(" ")

    if actions[0] == "TakeOdd":
        new_password = ""
        for index, ch in enumerate(password):
            if index % 2 != 0:
                new_password += ch
        password = new_password
        print(password)

    elif actions[0] == "Cut":
        start_index = int(actions[1])
        end_index = int(actions[2])
        password = password[:start_index] + password[start_index+end_index:]
        print(password)
    elif actions[0] == "Substitute":
        old = actions[1]
        new=actions[2]
        if old in password:
            password=password.replace(old,new)
            print(password)
        else:
            print("Nothing to replace!")
