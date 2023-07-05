FIRST_COUNT = 5
numbers = [ int(x) for x in input().split()]
avg_num = sum(numbers) / len(numbers)
filtered_numbers = sorted([ x for x in numbers if x > avg_num])

if not filtered_numbers:
    print("No")
else:
    # for i in range(FIRST_COUNT):
    #     if filtered_numbers:
    #         print(filtered_numbers.pop(),end=" ")
    print(*[filtered_numbers.pop() for i in range(FIRST_COUNT) if filtered_numbers])