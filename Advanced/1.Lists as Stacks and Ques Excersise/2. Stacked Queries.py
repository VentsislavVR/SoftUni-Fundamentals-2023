#  BEST WAY is the lambda way
from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}
for _ in range(int(input())):
    numbers_data = [int(x) for x in input().split()]
    # numbers_data = map(int,input().split())
    map_functions[numbers_data[0]](numbers_data)

numbers.reverse()
print(*numbers, sep=", ")

# FIRST
# from collections import deque
#
#
# numbers = deque()
# for _ in range(int(input())):
#     queries = input().split()
#     if queries[0] == "1":
#         number = int(queries[1])
#         numbers.append(number)
#     elif queries[0] == "2":
#         if numbers:
#             numbers.pop()
#     elif queries[0] == "3":
#         print(max(numbers))
#     elif queries[0] == "4":
#         print(min(numbers))
# result = [str(x) for x in numbers]
# result.reverse()
# print(', '.join(result))


# from collections import deque
# # SECOND
# numbers = deque()
# for _ in range(int(input())):
#     numbers_data = [int(x) for x in input().split()]
#     # numbers_data = map(int,input().split())
#     command = numbers_data[0]
#     if command == 1:
#         numbers.append(numbers_data[1])
#     elif command == 2:
#         if numbers:
#             numbers.pop()
#     elif command == 3:
#         if numbers:
#             print(max(numbers))
#     elif command == 4:
#         if numbers:
#             print(min(numbers))
# numbers.reverse()
# print(*numbers,sep=", ")
