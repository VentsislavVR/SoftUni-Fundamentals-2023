# 1st
# def remove_vowels_from_text(text):
#     forbidden_letters = ['a', 'o', 'u', 'e', 'i']
#     result = [char for char in text if char.lower() not in forbidden_letters]
#     return "".join(result)
#
#
# text = input()
# print(remove_vowels_from_text(text))
#2nd
# n_wagons = int(input())
# train = [0] * n_wagons
# commands = input()
#
# while commands != "End":
#     action = commands.split()[0]
#     if action == "add":
#         n_people = int(commands.split()[1])
#         train[-1] += n_people
#     elif action == "insert":
#         index = int(commands.split()[1])
#         n_people = int(commands.split()[2])
#         train[index] += n_people
#     elif action == "leave":
#         index = int(commands.split()[1])
#         n_people = int(commands.split()[2])
#         train[index] -= n_people
#
#     commands = input()
# print(train)
#3rd
# to_to_list = [0] * 10
# command = input()
#
# while command != "End":
#     importance, task = command.split("-")
#     importance = int(importance)
#     index = importance - 1
#     to_to_list[index] = task
#     command = input()
# print([task for task in to_to_list if task !=0])

#4th
# names = input().split(", ")
#
# sorted_names=sorted(names,key=lambda x:( -len(x),x))
# print(sorted_names)
#6th
# nums = list(map(int,input().split(', ')))
# print([index for index in range(len(nums))if nums[index]%2==0])
#5th
