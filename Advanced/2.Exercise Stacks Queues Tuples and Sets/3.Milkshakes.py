from collections import deque

chocolates = deque([int(c) for c in input().split(",")])
cups_of_milk = deque([int(m) for m in input().split(",")])

chocolate_milkshakes = 0

while chocolates and cups_of_milk and chocolate_milkshakes !=5:
    current_choc = chocolates.pop()
    current_cup = cups_of_milk.popleft()

    if current_cup <=0 and current_choc <=0:
        continue
    elif current_choc <= 0:
        cups_of_milk.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolates.append(current_choc)
        continue

    if current_choc == current_cup:
        chocolate_milkshakes += 1
    else:
        cups_of_milk.append(current_cup)
        current_choc -= 5
        chocolates.append(current_choc)
if chocolate_milkshakes >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")

