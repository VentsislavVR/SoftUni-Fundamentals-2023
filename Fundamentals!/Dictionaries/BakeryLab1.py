# data = input().split()
# products = {}
# for index in range(0,len(data),2):
#     key = data[index]
#     value = int(data[index+1])
#     products[key] = value
#
#
# print(products)

items = input().split()
bakery = {}

for index in range(0,len(items),2):
    bakery[items[index]] = int(items[index+1])
print(bakery)
# for key,value in bakery.items():
#     print(f"The Key is {key}, and the value is {value}")