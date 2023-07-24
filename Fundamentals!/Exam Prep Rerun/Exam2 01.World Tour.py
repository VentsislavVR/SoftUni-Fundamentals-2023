initial_stops = input()


while True:
    command = input().split(":")
    if command[0]=="Travel":
        print(f"Ready for world tour! Planned stops: {initial_stops}")
        break
    elif command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index <= len(initial_stops):
            initial_stops = initial_stops[:index] + string + initial_stops[index:]
            print(initial_stops)

    elif command[0] == "Remove Stop":
        start_idx = int(command[1])
        end_idx = int(command[2])
        if 0 <= start_idx <= end_idx < len(initial_stops):
            initial_stops = initial_stops[:start_idx] + initial_stops[end_idx+1:]
            print(initial_stops)
        else:
            print(initial_stops)


    elif command[0] == "Switch":
        old = command[1]
        new = command[2]
        if old in initial_stops:
            initial_stops = initial_stops.replace(old,new)
            print(initial_stops)
        else:
            print(initial_stops)


