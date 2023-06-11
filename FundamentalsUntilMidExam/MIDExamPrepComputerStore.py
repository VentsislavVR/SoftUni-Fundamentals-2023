current_sum = 0

is_special = False
while True:
    command = input()
    if command == "special":
        is_special = True
        break
    elif command == 'regular':
        break
    price = float(command)
    if price <= 0:
        print("Invalid price!")
        continue
    current_sum += price
    # if current_sum == 0:
    #     print("Invalid order!")
total = current_sum * 1.20
if is_special:
    total *= 0.90
if current_sum == 0:
    print("Invalid order!")
    exit()

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {current_sum:.2f}$")
print(f"Taxes: {current_sum*0.20:.2f}$")
print(f"-----------")
print(f"Total price: {total:.2f}$")