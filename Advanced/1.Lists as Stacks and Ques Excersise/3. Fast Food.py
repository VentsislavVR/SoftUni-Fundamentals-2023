from collections import deque
# DILQN
food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if food >= order:
        orders.popleft()
        food -= order
    else:
        print(f"Orders left: {' '.join(str(x) for x in orders)}")
        break

else:
    print("Orders complete")




## MY WAY
# quantity_of_food = int(input())
#
# orders = deque(int(x) for x in input().split())
# biggest = max(orders)
# print(biggest)
#
# while orders:
#     if quantity_of_food <= orders[0]:
#         break
#     quantity_of_food -= orders.popleft()
#
# if orders:
#     left = [str(x) for x in orders]
#     print(f"Orders left: {' '.join(left)}")
# else:
#     print("Orders complete")