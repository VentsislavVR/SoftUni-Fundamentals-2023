bakery = {}
items= input().split()

for index in range(0, len(items), 2):
    key = items[index]
    value = items[index + 1]
    bakery[key] = value

searched_products = input().split()

for product in searched_products:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")