message = input().split()
command_list = input().split()

while command_list != "3:1":
    command = command_list[0]

    if command == "merge":
        start_index = command[1]
        end_index = command[2]
