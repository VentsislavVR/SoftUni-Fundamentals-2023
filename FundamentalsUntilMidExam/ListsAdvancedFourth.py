# 4th
# input
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
# output
# Positive: 1, 0, 5, 3, 4, 12, 19
# Negative: -2, -100, -20, -33
# Even: -2, 0, 4, -100, -20, 12
# Odd: 1, 5, 3, 19, -33
def positive(some_numbers):
    return [number for number in some_numbers if int(number) >= 0]


def negative(some_numbers):
    return [number for number in some_numbers if int(number) < 0]


def even(some_numbers):
    return [number for number in some_numbers if int(number)%2 == 0]


def odd(some_numbers):
    return [number for number in some_numbers if int(number) % 2 != 0 and abs(int(number))>0]


numbers = input().split(', ')

print(f"Positive: {', '.join(positive(numbers))} ")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")