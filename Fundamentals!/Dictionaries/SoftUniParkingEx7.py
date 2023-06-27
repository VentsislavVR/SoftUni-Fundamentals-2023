# 1.1

# parking = {}
# number_of_cars = int(input())
# for car in range(number_of_cars):
#     current_driver = input().split()
#     action = current_driver[0]
#     if action == "register":
#         username = current_driver[1]
#         license_plate = current_driver[2]
#         if username in parking.keys():
#             print(f"ERROR: already registered with plate number {license_plate}")
#         else:
#             print(f"{username} registered {license_plate} successfully")
#             parking[username] = license_plate
#     elif action == "unregister":
#         username = current_driver[1]
#         if username not in parking:
#             print(f"ERROR: user {username} not found")
#         else:
#             print(f"{username} unregistered successfully")
#             # parking.pop(username)
#             del parking[username]
# for username,license_plate in parking.items():
#
#     print(f"{username} => {license_plate}")
# 1.2
# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
license_plate_by_username = {}
count = int(input())

for _ in range(count):
    command_args = input().split()
    command = command_args[0]
    name = command_args[1]
    if command == "register":
        license_plate = command_args[2]
        if name in license_plate_by_username:
            print(f"ERROR: already registered with plate number {license_plate_by_username[license_plate]}")
        else:
            license_plate_by_username[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
    elif command == "unregister":
        if name not in license_plate_by_username:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            license_plate_by_username.pop(name)

for key,value in license_plate_by_username.items():
    print(f"{key} => {value}")




