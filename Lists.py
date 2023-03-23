
# FIRST
# tail = input()
# body = input()
# head = input()
#
# zoo_list=[head,body,tail]
#
# print(zoo_list)

# SECOND

# n = int(input())
# courses=[]
# for _ in range(n):
#     course_name=input()
#     courses.append(course_name)
#
# print(courses)

# THIRD
# n = int(input())
# positive_numbers = []
# negative_numbers = []
#
# for _ in range(n):
#     numbers=int(input())
#     if numbers >=0:
#         positive_numbers.append(numbers)
#     else:
#         negative_numbers.append(numbers)
# print(positive_numbers)
# print(negative_numbers)
# print(f"Count of positives: {len(positive_numbers)}")
# print(f"Sum of negatives: {sum(negative_numbers)}")

# FOURTH
# n = int(input())
# word = input()
# all_strings=[]
# strings_containing_words = []
#
# for _ in range(n):
#     current_string=input()
#     all_strings.append(current_string)
#     if word in current_string:
#         strings_containing_words.append(current_string)
# print(all_strings)
# print(strings_containing_words)
# FIFTH
# n = int(input())
# positive_nums = []
# negative_nums = []
# even_nums = []
# odd_nums = []
# for _ in range(n):
#     current_number = int(input())
#     if current_number >= 0:
#         positive_nums.append(current_number)
#     else:
#         negative_nums.append(current_number)
#     if current_number % 2 == 0:
#         even_nums.append(current_number)
#     else:
#         odd_nums.append(current_number)
# command=input()
#
# if command == "even":
#     print(even_nums)
# elif command == "odd":
#     print(odd_nums)
# elif command == "positive":
#     print(positive_nums)
# else:
#     print(negative_nums)

# FIFTH 2.0
# n = int(input())
# all_numbers = []
# filtered = []
# for _ in range(n):
#     current_number = int(input())
#     all_numbers.append(current_number)
#
# command = input()
#
#
# for element in all_numbers:
#
#     if command == "even":
#         if element % 2 == 0:
#             filtered.append(element)
#     elif command == "odd":
#         if element % 2 != 0:
#             filtered.append(element)
#     elif command == "positive":
#         if element>=0:
#             filtered.append(element)
#     elif command == "negative":
#         if element <0:
#             filtered.append(element)
# print(filtered)






