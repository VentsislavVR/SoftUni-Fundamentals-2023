# 3rd
# Inventory

def inventory_func(items):
    while True:
        command_data = input()
        if command_data == "Craft!":
            break
        command, product = command_data.split(" - ")

        if command == "Collect":
            if product not in items:
                items.append(product)

        elif command == "Drop":
            if product in items:
                items.remove(product)
        elif command == "Combine Items":
            old_item, new_item = product.split(":")
            if old_item in items:
                old_item_index = items.index(old_item)
                items.insert(old_item_index+1, new_item)
        elif command == "Renew":
            if product in items:
                items.remove(product)
                items.append(product)
    print(", ".join(items))


data = input().split(", ")

inventory_func(data)
