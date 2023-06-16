def find_minimum(numbers):
    return min(numbers)


def find_maximum(numbers):
    return max(numbers)


def calculate_sum(numbers):
    return sum(numbers)


numbers = input().split()

numbers = [int(num) for num in numbers]

minimum_number = find_minimum(numbers)
maximum_number = find_maximum(numbers)
sum_numbers = calculate_sum(numbers)

print("The minimum number is:", minimum_number)
print("The maximum number is:", maximum_number)
print("The sum of all numbers is:", sum_numbers)
