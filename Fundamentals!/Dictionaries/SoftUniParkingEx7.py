parking = {}
number_of_cars = int(input())
for car in range(number_of_cars):
    current_driver = input().split()
    action = current_driver[0]
    if action == "register":
        username = current_driver[1]
        license_plate = current_driver[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            print(f"{username} registered {license_plate} successfully")
            parking[username] = license_plate
    elif action == "unregister":
        username = current_driver[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            # parking.pop(username)
            del parking[username]
for username,license_plate in parking.items():

    print(f"{username} => {license_plate}")

    

# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
