# 1st
# def smallest_number(numbers):
#     min_number = min(numbers)
#     return min_number
#
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# all_numbers = [first_number,second_number,third_number]
# min_numbers = smallest_number(all_numbers)
# print(min_numbers)
# 2nd
# def sum_numbers(first,second):
#     return first + second
#
#
# def subtract(sum, third):
#     return sum - third
#
#
# def add_and_subtract(first, second, third):
#     sum_of_first_and_second = sum_numbers(first_number, second_number)
#     result = subtract(sum_of_first_and_second, third)
#     return  result
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# print(add_and_subtract(first_number, second_number, third_number))
# 3rd
# def collect_character(first, second):
#     characters = []
#     for current_character in range(ord(first) + 1, ord(second)):
#         characters.append(chr(current_character))
#     return characters
#
#
# first_character = input()
# second_character = input()
# result = collect_character(first_character, second_character)
# print(" ".join(result))
# 4th
# def even_and_odd_numbers(number):
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#     for digit in number:
#         if int(digit) % 2 == 0:
#             sum_of_even_digits += int(digit)
#         else:
#             sum_of_odd_digits += int(digit)
#     return sum_of_odd_digits, sum_of_even_digits
#
#
# number_as_string = input()
# sum_of_odd_digits, sum_of_even_digits = even_and_odd_numbers(number_as_string)
# print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
# 9th

# def password_validation(some_password):
#     pass_is_valid = True
#     if len(some_password) < 6 or len(some_password) > 10:
#         print("Password must be between 6 and 10 characters")
#         pass_is_valid = False
#     if not some_password.isalnum():
#         print("Password must consist only of letters and digits")
#         pass_is_valid = False
#     digit_counter = 0
#     for character in some_password:
#         if character.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         print("Password must have at least 2 digits")
#         pass_is_valid = False
#     return pass_is_valid
#
#
# password = input()
# password_is_valid = password_validation(password)
# if password_is_valid:
#     print("Password is valid")
# 10th
# def is_perfect(some_number):
#     sum = 0
#     for divisor in range(1,some_number):
#         if some_number % divisor == 0:
#             sum += divisor
#     if sum == some_number:
#         return "We have a perfect number!"
#     return "It's not so perfect."
#
#
# number = int(input())
# print(is_perfect(number))
# 12th
# def factorial(number):
#     for current_number in range(1,number):
#         number *= current_number
#     return number
#
#
# first_number = int(input())
# second_number = int(input())
# first_number_factorial = factorial(first_number)
# second_number_factorial = factorial(second_number)
# final_result = first_number_factorial / second_number_factorial
# print(f"{final_result:.2f}")
# 11thLoadingBar
# def status(number):
#     if number == 100:
#         return "100% Complete!\n[%%%%%%%%%%]"
#     return f"{number}% [{(number//10) * '%'}{(10 -(number//10)) * '.'}]""" \
#            "\nStill loading..."
#
#
# single_number = int(input())
# print(status(single_number))
# 5th
#
# even_nums = input().split()
#
#
# def myFunc(x):
#     if int(x) % 2 == 0:
#         return True
#     else:
#         return False
#
#
# adults = filter(myFunc, even_nums)
# even_result = []
# for x in adults:
#     even_result.append(int(x))
# print(even_result)
# 6th

# def sorting_func(nums):
#   sorted=[]
#   for s in sorted_nums:
#     sorted.append(s)
#   return  sorted

# def sorting_func(num):
#     new_arangment = []
#     for x in num:
#         new_arangment.append(int(x))
#         x = sorted(new_arangment)
#     return x
#
#
# sorted_nums = input().split()
#
# print(sorting_func(sorted_nums))

# 7th

#
# numbers = input()
# numbers_list = [int(num) for num in numbers.split()]
#
# minimum = min(numbers_list)
# maximum = max(numbers_list)
# total = sum(numbers_list)
#
# print(f"The minimum number is {minimum}")
# print(f"The maximum number is {maximum}")
# print(f"The sum number is: {total}")
# 8th
# def is_it(n):
#     poli_list = []
#
#     for i in n:
#         if i[0::] == i[::-1]:
#             poli = True
#             poli_list.append(poli)
#         else:
#             poli = False
#             poli_list.append(poli)
#
#     return poli_list
#
#
# nums = input().split(", ")
#
# result = is_it(nums)
# for i in result:
#     print(i)