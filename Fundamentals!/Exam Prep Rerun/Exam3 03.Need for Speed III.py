def drive(garage, info):
    car, miles, fuel = info[0], int(info[1]), int(info[2])
    if car in garage.keys():
        if garage[car]["fuel"] >= fuel:
            garage[car]["fuel"] -= fuel
            garage[car]["miles"] += miles
            print(f"{car} driven for {miles} kilometers. {fuel} liters of fuel consumed.")
        else:
            print(f"Not enough fuel to make that ride")
    if garage[car]['miles'] >= 100_000:
        print(f'Time to sell the {car}!')
        del garage[car]
    return garage


def refuel(garage, info):
    car, fuel = info[0], int(info[1])
    tank_cap = 75
    current_fuel = garage[car]['fuel']
    garage[car]["fuel"] += int(fuel)
    if garage[car]["fuel"] > tank_cap:
        garage[car]["fuel"] = tank_cap
        print(f"{car} refueled with {tank_cap - current_fuel} liters")
    else:
        print(f"{car} refueled with {fuel} liters")
    return garage


def revert(garage, info):
    car, kmh = info[0], int(info[1])
    garage[car]['miles'] -= kmh
    if garage[car]['miles'] < 10_000:
        garage[car]['miles'] = 10_000
    else:
        print(f"{car} mileage decreased by {kmh} kilometers")
    return garage


def get_input(number_of_c):
    garage = {}
    for car in range(number_of_c):
        car, mileage, fuel = input().split("|")
        garage[car] = {"miles": int(mileage), "fuel": int(fuel)}
    return garage


def result(garage):
    for car, stats in garage.items():
        print(f"{car} -> Mileage: {garage[car]['miles']} kms, Fuel in the tank: {garage[car]['fuel']} lt.")


def the_game(number_of_c):
    garage = get_input(number_of_c)

    while True:
        line = input()
        if line == "Stop":
            result(garage)
            break
        actions, *info = line.split(" : ")

        if actions == "Drive":
            drive(garage, info)
        elif actions == "Refuel":
            refuel(garage, info)
        elif actions == "Revert":
            revert(garage, info)


number_of_cars = int(input())
the_game(number_of_cars)
