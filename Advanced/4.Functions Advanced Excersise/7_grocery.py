def grocery_store(**products):
    products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    # return '\n'.join([f"{key}: {value}" for key,value in products])
    result = []
    for product, quantity in products:
        result.append(f"{product}: {quantity}")

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
