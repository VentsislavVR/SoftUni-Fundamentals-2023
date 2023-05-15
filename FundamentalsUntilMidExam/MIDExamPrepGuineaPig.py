#1st
# GUINEA PIG
# •	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]

food_quantity = float(input())*1000
hay_quantity = float(input())*1000
cover_quantity = float(input())*1000
guineas_weight = float(input())*1000
flag = False
for day in range(1,31):
    food_quantity -= 300

    if day % 2 == 0:
        hay_quantity -= food_quantity * 0.05

    if day % 3 == 0:
        cover_quantity -= guineas_weight / 3
    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        flag = True
        break


if not flag:
    food,hay,cover = food_quantity /1000 , hay_quantity / 1000,cover_quantity/1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")

else:
    print("Merry must go to the pet store!")