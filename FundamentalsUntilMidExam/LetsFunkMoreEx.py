# 1st
# def data_type_check(c,n):
#     result = ""
#     if c == "int":
#         result = int(n) * 2
#     elif c == "real":
#         result = f'{float(n) * 1.50:.2f}'
#     elif c == "string":
#         result= f'${n}$'
#     return result
#
#
# comand = input()
# num_or_str= input()
# print(data_type_check(comand,num_or_str))

# 2nd
# from math import floor
# def deba_shibani_afasfsf(first, second, third, fourth):
#     x = 0
#     y = 0
#     if abs(first) > abs(third):
#         x =int(floor(third))
#     else:
#         x = int(floor(first))
#     if abs(second) > abs(fourth):
#         y = int(floor(fourth))
#     else:
#         y = int(floor(second))
#     # closest_x = min(x,key=abs())
#     # closest_y = min(y,key=abs())
#
#     return f"({x}, {y})"
#
#
# X1 = float(input())
# Y1 = float(input())
# X2 = float(input())
# Y2 = float(input())
# print(deba_shibani_afasfsf(X1, Y1, X2, Y2))
#4th
# def tribonacci(n):
#     a, b, c = 1, 1, 2
#     sequence = [a, b, c]
#     while len(sequence) < n:
#         next_number = a + b + c
#         sequence.append(next_number)
#         a, b, c = b, c, next_number
#     return " ".join(str(num) for num in sequence)
#
#
# number = int(input())
# result = tribonacci(number)
# print(result)

# #5th
# def pos_neg(fi,se,th):
#     result = ""
#     if fi < 0 or se < 0 or th < 0:
#         result = "negative"
#     elif fi == 0 or se == 0 or th == 0:
#         result = 'zero'
#     else:
#         result = 'positive'
#     return result
#
#
# first = int(input())
# second = int(input())
# third = int(input())
# print(pos_neg(first,second,third))