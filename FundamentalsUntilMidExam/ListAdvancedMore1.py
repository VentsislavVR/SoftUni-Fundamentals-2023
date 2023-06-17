# population = [int(x) for x in input().split(", ")]
# minimum_wealth = int(input())
#
# total_wealth = sum(population)
# if total_wealth < (minimum_wealth * len(population)):
#     print("No equal distribution possible")
# else:
#     amount_to_give = 0
#     rich = [x for x in population if x >= minimum_wealth]
#     poor = [x for x in population if x < minimum_wealth]
#
#
#     print(poor)

population = [int(num) for num in input().split(", ")]
wealth_level = int(input())

if sum(population) < len(population) * wealth_level:
    print('No equal distribution possible')
else:
    poorest = min(population)

    while poorest < wealth_level:
        poorest_index = population.index(poorest)
        richest = max(population)
        richest_index = population.index(richest)

        needed = wealth_level - poorest
        can_take = richest - wealth_level
        redistributed_wealth = min(needed, can_take)
        population[poorest_index] += redistributed_wealth
        population[richest_index] -= redistributed_wealth

        poorest = min(population)

    print(population)