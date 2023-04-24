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
#5th

