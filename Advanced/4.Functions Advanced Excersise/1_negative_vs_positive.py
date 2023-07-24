def print_numbers(positive,negative):
    print(negative)
    print(positive)

    if abs(positive) > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


nums = [int(x) for x in input().split()]
positive_numbers = sum(x for x in nums if x > 0)
negative_numbers = sum(x for x in nums if x < 0)
print_numbers(positive_numbers,negative_numbers)


