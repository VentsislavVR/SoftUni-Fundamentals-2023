price_by_product={}
quantity_by_product = {}

while True:
    line = input()

    if line == "buy":
        break
    args = line.split()
    product = args[0]
    price = float(args[1])
    quantity = int(args[2])

    if product in price_by_product:
        price_by_product[product] = price
        quantity_by_product[product] += quantity
    else:
        price_by_product[product] = price
        quantity_by_product[product] = quantity

for product in price_by_product:
    price = price_by_product[product]
    quantity = quantity_by_product[product]

    print(f"{product} -> {price*quantity:.2f}")
