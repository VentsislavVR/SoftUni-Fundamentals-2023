def sorted_func(greater_numbers_than_average):
    top_five_numbers = []
    for num in sorted(greater_numbers_than_average)[::-1]:
        if len(top_five_numbers) < 5:
            top_five_numbers.append(num)
        else:
            break
    return " ".join([str(num) for num in top_five_numbers])


def numbers_func(numbers):
    average_sum = sum(numbers) / len(numbers)
    greater_numbers_than_average = [num for num in numbers if num > average_sum]

    if greater_numbers_than_average:
        print(sorted_func(greater_numbers_than_average))
    else:
        print("No")


nums = [int(x) for x in input().split(" ")]
numbers_func(nums)
