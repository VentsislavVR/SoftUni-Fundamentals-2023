def drive_func(garage,car,distance,fuel):
    if car in garage:
        if garage[car]["fuel"] >= fuel:
            garage[car]["mile"] += distance
            garage[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
    if garage[car]["mile"] >= 100_000:
        print(f"Time to sell the {car}!")
        del garage[car]
    return garage
def refuel_func(garage,car,fuel):
    max_cap = 75
    if car in garage:
        garage[car]["fuel"] += fuel
        if garage[car]["fuel"] > max_cap:
            print(f"{car} refueled with {max_cap-(garage[car]['fuel'] -fuel)} liters")
            garage[car]["fuel"] = max_cap
        else:
            print(f"{car} refueled with {fuel} liters")
    return garage
def revert_func(garage,car,kmh):
    if car in garage:
        garage[car]["mile"] -= kmh
        if garage[car]["mile"] <= 10_000:
            garage[car]["mile"] = 10_000
        else:
            print(f"{car} mileage decreased by {kmh} kilometers")
    return garage

garage_count = int(input())
garage = {}
for cars in range(garage_count):
    my_babies = input().split("|")
    car = my_babies[0]
    mileage = int(my_babies[1])
    fuel_in_tank = int(my_babies[2])
    garage[car] ={"mile":mileage,"fuel":fuel_in_tank}


while True:
    line = input()
    if line == "Stop":
        break
    command = line.split(" : ")

    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        garage = drive_func(garage,car,distance,fuel)
    elif command[0]=="Refuel":
        car=command[1]
        fuel = int(command[2])
        garage = refuel_func(garage,car,fuel)
    elif command[0]=="Revert":
        car = command[1]
        kmh = int(command[2])
        garage = revert_func(garage,car,kmh)


for cars in garage:
    print(f"{cars} -> Mileage: {garage[cars]['mile']} kms, Fuel in the tank: {garage[cars]['fuel']} lt.")

