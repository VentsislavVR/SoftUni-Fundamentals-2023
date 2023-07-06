import re

# pattern = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]*[\?.0-9]+)[\!](?P<quontity>[0-9])"
pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
total_price = 0
bought_items = []
while True:
    line = input()
    if line == "Purchase":
        break
    match = re.findall(pattern, line)
    if not match:
        continue
    groups = match[0]
    item = groups[0]
    price = float(groups[1])
    quantity = int(groups[3])
    bought_items.append(item)
    total_price+= quantity * price

print("Bought furniture:")
for product in bought_items:
    print(product)
print(f"Total money spend: {total_price:.2f}")


###### GROUPdict !!
# import re
#
# # pattern = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]*[\?.0-9]+)[\!](?P<quontity>[0-9])"
# pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
# total_price = 0
# bought_items = []
# while True:
#     line = input()
#     if line == "Purchase":
#         break
#     match = re.match(pattern, line)
#     if not match:
#         continue
#     groups = match.groupdict()
#     bought_items.append(groups["furniture"])
#     total_price += float(groups["price"]) * int(groups["quantity"])
#
#
# print("Bought furniture:")
# for product in bought_items:
#     print(product)
# print(f"Total money spend: {total_price:.2f}")