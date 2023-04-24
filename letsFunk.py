# 1st
# num_as_string= input().split()
#
# res = []
#
# for num in num_as_string:
#     res.append(abs(float(num)))
# print(res)
# 2nd
# def grade_to_word(grade):
#     if 2.00 <= grade <= 2.99:
#         print("Fail")
#     elif 3.00 <= grade <= 3.49:
#         print("Poor")
#     elif 3.50 <= grade <= 4.49:
#         print("Good")
#     elif 4.50 <= grade <= 5.49:
#         print("Very Good")
#     elif 5.50 <= grade <= 6.00:
#         print("Excellent")
#
#
# grade = float(input())
# grade_to_word(grade)
# 3rd
# def calculate(command, first_num, second_num):
#     result = 0
#     if command == "multiply":
#         result = first_num * second_num
#     elif command == "divide":
#         result = first_num / second_num
#     elif command == "add":
#         result = first_num + second_num
#     elif command == "subtract":
#         result = first_num - second_num
#     return result
#
#
# command_operator = input()
# num_1 = int((input()))
# num_2 = int(input())
#
# result = calculate(command_operator, num_1, num_2)
# print(int(result))
# 3rd
# text = input()
# n = int(input())
#
# repeat_as_lamda = lambda word,times:word*times
# print(repeat_as_lamda(text,n))
# 4th

# def calculate_total_amount(product, quantity):
#     total_amount = 0
#
#     if product == "water":
#         total_amount = quantity * 1
#     elif product == "coffee":
#         total_amount = quantity * 1.50
#     elif product == "coke":
#         total_amount = quantity * 1.40
#     elif product == "snacks":
#         total_amount = quantity * 2.00
#     return total_amount
#
#
# product_to_buy = input()
# requested_quantity = int(input())
# result = calculate_total_amount(product_to_buy, requested_quantity)
# print(f"{result:.2f}")
#6th
# def rectangle_area(width,height):
#     result = width * height
#     return result
#
# a = int(input())
# b= int(input())
#
# print(rectangle_area(a,b))
#7th

# nums = input().split()
# res = []
# for i in nums:
#     res.append(round(float(i)))
# print(res)

def ro(nums):
    res = []
    for i in nums:
        res.append(round(float(i)))
    return res


print(ro(input().split()))
