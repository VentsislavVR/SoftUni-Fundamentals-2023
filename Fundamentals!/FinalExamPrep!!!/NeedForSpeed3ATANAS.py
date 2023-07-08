cars_count = int(input())

fuel_by_car = {}
mileage_by_car = {}

for _ in range(cars_count):
    cars_arguments = input().split("|")
    car = cars_arguments[0]
    mileage = int(cars_arguments[1])
    fuel = int(cars_arguments[2])

    fuel_by_car[car] = fuel
    mileage_by_car[car]=mileage

while True:
    line =  input()
    if line == 'Stop':
        break
    command_args = line.split(" : ")
    command = command_args[0]
    car = command_args[1]

    if command == 'Drive':
        distance = int(command_args[2])
        fuel = int(command_args[3])

        if fuel > fuel_by_car[car]:
            print("Not enough fuel to make that ride")
            continue
        fuel_by_car[car] -= fuel
        mileage_by_car[car] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if mileage_by_car[car] >= 100000:
            fuel_by_car.pop(car)
            mileage_by_car.pop(car)
            print(f"Time to sell the {car}!")
    elif command == 'Refuel':
        fuel = int(command_args[2])
        fuel_before_refuel = fuel_by_car[car]
        fuel_by_car[car] = min(fuel_by_car[car]+fuel,75)
        print(f"{car} refueled with {fuel_by_car[car]-fuel_before_refuel} liters")
    else:
        kilometers = int(command_args[2])
        updated_miliage = mileage_by_car[car] - kilometers
        if updated_miliage < 10000:
            mileage_by_car[car] = 10000
        else:
            mileage_by_car[car] = updated_miliage
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in fuel_by_car.keys():
    fuel = fuel_by_car[car]
    mileage = mileage_by_car[car]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")