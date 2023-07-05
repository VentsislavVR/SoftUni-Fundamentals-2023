# population = [int(x) for x in input().split(", ")]
# minimum_wealth = int(input())
#
# total_wealth = sum(population)
# if total_wealth < (minimum_wealth * len(population)):
#     print("No equal distribution possible")
# else:
#     distributed_wealth = []
#     for dis in population:
#         if dis < minimum_wealth:
#             dis += minimum_wealth - dis
#             distributed_wealth.append(dis)
#         else:
#             dis
#     print(distributed_wealth)

numbers = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())
#
for i in range(len(numbers)):
    if numbers[i] < minimum_wealth:
        c = minimum_wealth - numbers[i]
        max_number = max(numbers)
        if max_number - c >= minimum_wealth:
            numbers[numbers.index(max_number)] -= c
            numbers[i] += c
if sum(numbers) >= len(numbers) * minimum_wealth:
    print(numbers)
else:
    print("No equal distribution possible")