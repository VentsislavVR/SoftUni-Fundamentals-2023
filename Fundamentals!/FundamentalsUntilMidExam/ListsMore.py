# numbers=input().split(",")
#
# new_list = []
# for zero in numbers:
#     if int(zero) == 0:
#         numbers.remove(zero)
#         numbers.append(zero)
# for chisla in numbers:
#     new_list.append(int(chisla))
# print(new_list)
# SECOND

# numbers = input().split()
# text = input()
# message = ""
# for number in numbers:
#     sum_of_digits = 0
#     for digit in number:
#         sum_of_digits += int(digit)
#     index = sum_of_digits % len(text)
#     char = text[index]
#     message += char
#     text = text[:index] + text[index + 1:]
# print(message)

#
#
# numbers = input().split()
# text = input()
# message = ""
# for number in numbers:
#     sum_of_digits = sum(int(digit) for digit in number)
#     index = sum_of_digits % len(text)
#     char = text[index]
#     message += char
#     text = text.replace(char, "", 1)
# print(message)

# numbers = input().split()
# text = input()
# message = ""
# for number in numbers:
#     sum_of_digits = 0
#     for digit in number:
#         sum_of_digits += int(digit)
#     index = sum_of_digits % len(text)
#     char = text[index]
#     message += char
#     text = text[:index] + text[index + 1:]
# print(message)

# # THIRD
# numbers = input().split()
# middle_index = len(numbers) // 2
# left_time = 0
# right_time = 0
# for i in range(len(numbers)):
#     if i == middle_index:
#         continue
#     if int(numbers[i]) == 0:
#         if i < middle_index:
#             left_time *= 0.8
#         else:
#             right_time *= 0.8
#     if i < middle_index:
#         left_time += int(numbers[i])
#     else:
#         right_time += int(numbers[i])
# if left_time > right_time:
#     winner="right"
#     total_time=right_time
# else:
#     winner= "left"
#     total_time=left_time
# print(f"The winner is {winner} with total time: {total_time:.1f}")
#fourth
# people = input().split()
# skip = int(input())
#
# killing_streak = []
# i = 0
# while len(people)>0:
#     i =(i + skip - 1) % len(people)
#     killing_streak.append(people.pop(i))
# result=[int(x) for x in killing_streak]
# print("["+",".join(killing_streak)+ "]")


#
# def josephus(lst, k):
#     executed = []
#     i = 0
#     while len(lst) > 0:
#         i = (i + k - 1) % len(lst)
#         executed.append(lst.pop(i))
#     return "[" + ",".join(str(x) for x in executed) + "]"
# lst = list(map(int, input().split()))
# k = int(input())
# print(josephus(lst, k))
# row1 = input().split()
# row2 = input().split()
# row3 = input().split()
# for row in [row1, row2, row3]:
#     if row == ['1', '1', '1']:
#         print("First player won")
#         break
#     elif row == ['2', '2', '2']:
#         print("Second player won")
#         break
# for col in range(3):
#     if row1[col] == row2[col] == row3[col] == '1':
#         print("First player won")
#         break
#     elif row1[col] == row2[col] == row3[col] == '2':
#         print("Second player won")
#         break
# if row1[0] == row2[1] == row3[2] == '1' or row1[2] == row2[1] == row3[0] == '1':
#     print("First player won")
# elif row1[0] == row2[1] == row3[2] == '2' or row1[2] == row2[1] == row3[0] == '2':
#     print("Second player won")
# else:
#     print("Draw!")
#bon
# num = int(input())
# prime = True
#
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
# else:
#     prime = False
# print(prime)
#6th

starting_list = input().split(" ")
numbers_list = [int(num) for num in starting_list]

command = input().split()
while command[0] != "end":
    manipulation = command[0]
    if manipulation == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(numbers_list):
            print("Invalid index")
        numbers_list = numbers_list[index + 1:] + numbers_list[:index + 1]
    elif manipulation == "max":
        max = float("-inf")
        if command[1] == "odd":
            for od in numbers_list:
                if od % 2 !=0 and od > max:
                    max = od
            if max == float("-inf"):
                print("No matches")
            else:
                print(numbers_list.index(max))
        elif command[1] == "even":
            for ev in numbers_list:
                if ev % 2 ==0 and ev > max:
                    max = ev
            if max == float("-inf"):
                print("No matches")
            else:
                print(numbers_list.index(max))
    elif manipulation == "min":
        min = float("inf")
        if command[1] == "odd":
            for od in numbers_list:
                if od % 2 !=0 and od < min:
                    min = od
            if min == float("inf"):
                print("No matches")
            else:
                print(numbers_list.index(min))
        elif command[1] == "even":
            for ev in numbers_list:
                if ev % 2 ==0 and ev < min:
                    min = ev
            if min == float("inf"):
                print("No matches")
            else:
                print(numbers_list.index(min))
    elif manipulation == "first":
        kount=[]
        count = command[1]
        if command[2] == "even":
            for c in numbers_list:
                if c % 2 == 0 and len(kount) <2:
                    kount.append(c)
            if int(count)>len(numbers_list):
                print("Invalid count")
            else:
                print(kount)
        elif command[2] == "odd":
            for c in numbers_list:
                if c % 2 != 0 and len(kount) <2:
                    kount.append(c)
            if int(count)>len(numbers_list):
                print("Invalid count")
            else:
                print(kount)
    elif manipulation == "last":
        kount =[]
        count = command[1]
        if command[2] == "even":
            for c in reversed(numbers_list):
                if c % 2 == 0 and len(kount) <2:
                    kount.append(c)
            if int(count)>len(numbers_list):
                print("Invalid count")
            else:
                print(kount)
        elif command[2] == "odd":
            for c in reversed(numbers_list):
                if c % 2 != 0 and len(kount) <2:
                    kount.append(c)
            if int(count)>len(numbers_list):
                print("Invalid count")
            else:
                print(kount)

    command=input().split()
print(numbers_list)