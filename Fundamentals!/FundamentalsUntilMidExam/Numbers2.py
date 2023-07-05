numbers = [int(x) for x in input().split()]


result = []

for num in numbers:
    avrage = sum(numbers) / len(numbers)
    if num > avrage:
        result.append(num)
if len(result) > 0:
    final = sorted(result,reverse=True)[:5]
    print(*final)
else:
    print("No")


