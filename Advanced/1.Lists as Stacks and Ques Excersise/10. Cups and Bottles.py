from collections import deque


cups_of_water = deque([int(x) for x in input().split()])
bottles_of_water = deque([int(x) for x in input().split()])

wasted_water = 0
while bottles_of_water and cups_of_water:
    bottle = bottles_of_water.pop()
    cup = cups_of_water.popleft()
    if bottle >= cup:
        wasted_water += bottle - cup
    elif bottle < cup:
        cup -= bottle
        cups_of_water.appendleft(cup)

if bottles_of_water:
    print(f"Bottles: {' '.join(str(x) for x in bottles_of_water)}")
if cups_of_water:
    print(f"Cups: {' '.join(str(x) for x in cups_of_water)}")

print(f"Wasted litters of water: {wasted_water}")