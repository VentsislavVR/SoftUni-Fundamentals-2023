budget = float(input())
flour_price_per_kg = float(input())
egg_price = flour_price_per_kg * 0.75
milk_price1l = flour_price_per_kg * 1.25

loaf_of_bread_price = egg_price +flour_price_per_kg + (milk_price1l/4)
number_of_loaves = 0
colored_eggs = 0
while budget > loaf_of_bread_price:
    budget -= loaf_of_bread_price
    number_of_loaves+= 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

