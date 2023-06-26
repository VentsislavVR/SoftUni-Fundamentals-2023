resources = {}

while True:
    line = input()
    if line == "stop":
        break

    quantity = int(input())
    if line not in resources:
        resources[line] = 0
    resources[line] += quantity

# for resource in resources:
#     print(f"{resource} -> {resources[resource]}")
results = print([f"{key} -> {value}" for key,value in resources.items()])