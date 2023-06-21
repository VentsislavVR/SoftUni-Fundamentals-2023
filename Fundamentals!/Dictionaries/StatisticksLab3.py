# products = {}
#
# data = input()
#
# while data != 'statistics':
#     key, value = data.split(": ")
#     value = int(value)
#     if key not in products:
#         products[key] = value
#     else:
#         products[key] += value
#     data = input()
#
# print("Products in stock:")
# for key, value in products.items():
#     print(f"- {key}: {value}")
# print(f"Total Products: {len(products)}")
# print(f"Total Quantity: {sum(products.values())}")
products = {}
command = input()

while command != "statistics":
    key,value = command.split(": ")

    if key not in products.keys():
        products[key] = 0
    products[key] += int(value)
    command = input()

print("Products in stock:")
for product , quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
# print(f"Total Quantity: {sum(products.values())}")
print(f"Total Quantity: {sum(int(s) for s in products.values())}")

