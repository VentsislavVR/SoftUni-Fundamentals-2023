food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
wight = float(input()) * 1000
all_good = True
for day in range(1, 31):
    food -= 300
    if day % 2 ==0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= wight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        all_good = False
        break
if all_good == False:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
