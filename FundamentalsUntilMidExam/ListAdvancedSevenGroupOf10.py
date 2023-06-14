# numbers = input().split(', ')
# number_list = [int(n) for n in numbers]
# number_list.sort()
#
# max_value = 10
# current_list = []
# for num in number_list:
#     if num < max_value:
#         current_list.append(num)
#     else:
#         print(f"Group of {max_value}'s: {current_list}")
#         current_list = [num]
#         max_value += 10
#
# if current_list:
#     print(f"Group of {max_value}'s: {current_list}")



# numbers = input().split(', ')
# max = 10
# while numbers:
#     result = [int(x) for x in numbers if int(x) < int(max)]
#     print(f"Group of {max}'s: {result}")
#     numbers.remove(x)
#     max +=10
numbers = input().split(', ')
maximum = 10
while numbers:
    result = [int(x) for x in numbers if int(x) <= maximum]
    print(f"Group of {maximum}'s: {result}")
    numbers = [x for x in numbers if int(x) > maximum]
    maximum += 10



