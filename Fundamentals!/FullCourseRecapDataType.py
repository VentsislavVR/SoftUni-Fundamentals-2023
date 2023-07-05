# first
# first_integer = int(input())
# second_integer = int(input())
# third_integer = int(input())
# fourth_integer = int(input())
# result = ((first_integer + second_integer) // third_integer ) * fourth_integer
# print(result)
#
# Char to string 2
# one,two,three = input(),input(),input()
#
# print(f"{one}{two}{three}")

# Elevator 3
# from math import ceil
# people=int(input())
# capacity = int(input())
#
# result = people /capacity
# print(ceil(result))

# #4th
# n = int(input())
# result = 0
# for i in range(n):
#     letter = input()
#     result+= ord(letter)
#
# print(f"The sum equals: {result}")
# 5

# start = int(input())
# end = int(input())
# result = ""
# for i in range(start,end+1):
#     result += chr(i) + " "
# print(result)
# 6th
# num = int(input())
#
# for i in range(0,num):
#     for j in range(0,num):
#         for k in range(0,num):
#             print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")
# capacity = 255
# num_of_lines = int(input())
#
# current_volume = 0
# for i in range(num_of_lines):
#     adding = int(input())
#     current_volume += adding
#     if current_volume > capacity:
#         print("Insufficient capacity!")
#         current_volume-=adding
# print(f"{current_volume}")

# from math import floor
# group_size = int(input())
# days = int(input())
#
# coins = 0
#
# for day in range(1, days + 1):
#     coins += 50
#     coins -= group_size *2
#
#     if day % 15 == 0:
#         group_size += 5
#         coins -= group_size * 2
#     if day % 10 == 0:
#         group_size -= 2
#     if day % 5 == 0:
#         coins += group_size * 20
#         # if day % 3 == 0:
#         #     coins -= group_size * 2
#     if day % 3 == 0:
#         coins -= group_size * 3
#
# print(f"{group_size} companions received {floor(coins/group_size)} coins each.")
#9th


# number_of_snowballs = int(input())
#
# snow_balls = []
#
# for ball in range(number_of_snowballs):
#     weight = int(input())
#     velocity = int(input())
#     quality = int(input())
#     best = (weight / velocity) ** quality
#     snow_balls.append([best,weight,velocity,quality])
# result = sorted(snow_balls)
#
# print(f"{result[-1][1]} : {result[-1][2]} = {result[-1][0]:.0f} ({result[-1][-1]})")
#10th

# lost_fight_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# expenses = 0
# shield_repair = 0
# for lost_fight in range(1,lost_fight_count+1):
#     if lost_fight % 2 == 0:
#         expenses += helmet_price
#     if lost_fight % 3 == 0:
#         expenses += sword_price
#     if lost_fight % 2 ==0 and lost_fight % 3 == 0:
#         expenses += shield_price
#         shield_repair += 1
#         if shield_repair % 2 == 0:
#             expenses += armor_price
#
#
#
# print(f"Gladiator expenses:{expenses:.2f} aureus")