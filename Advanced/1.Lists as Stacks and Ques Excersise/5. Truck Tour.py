# from collections import deque
# number_of_pumps = int(input())
# count_circles = []
# current_petrol = 0
# for pump in range(0,number_of_pumps):
#     data = input().split()
#     refilled_petrol = int(data[0])
#     distance_to_next_pump = int(data[1])
#     current_petrol +=refilled_petrol
#
#     if refilled_petrol >=distance_to_next_pump:
#
#         count_circles.append(pump)
#         continue
#     else:
#         pass
#
#
# print(min(count_circles))

from collections import deque

pumps_data = deque([[int(x)for x in input().split()] for _ in range(int(input()))])
pumps_data_copy = pumps_data.copy()
gas_in_tank = 0
index = 0
while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index +=1
        gas_in_tank=0
print(index)







