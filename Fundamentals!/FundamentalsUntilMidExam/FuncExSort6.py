def sorted_nums(numbers):
    result = []
    for n in numbers:
        result.append(int(n))
    return sorted(result)



numbers = input().split()
print(sorted_nums(numbers))