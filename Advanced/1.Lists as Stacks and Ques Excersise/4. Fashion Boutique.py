from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_space = int(input())

racks_count = 1
current_rack_space = rack_space

while clothes:
    cloth = clothes.pop()
    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = rack_space - cloth
print(racks_count)


# fail in this solution im filing the empty space 
# box_of_clothes = deque([int(x) for x in input().split()])
#
# rack_capacity = int(input())
# racks_filled = 0
# current_rack = 0
# for r in box_of_clothes.copy():
#
#     if current_rack + box_of_clothes[-1] < rack_capacity:
#         current_rack += box_of_clothes.pop()
#     elif current_rack + box_of_clothes[-1] >= rack_capacity:
#         racks_filled += 1
#         current_rack += box_of_clothes.pop()
#         remaining = current_rack - rack_capacity
#         current_rack = remaining
# print(racks_filled)
