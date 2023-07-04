number_of_items_to_buy = int(input())

days_until_christmas = int(input())
christmas_spirit = 0
money_spent = 0
for i in range(1,days_until_christmas+1):
    if i % 2 == 0:
        money_spent +=2  * number_of_items_to_buy
        christmas_spirit += 5
    if i % 3 == 0:
        money_spent += 8 * number_of_items_to_buy
        christmas_spirit += 13
    if i % 5 ==0:
        money_spent +=15 * number_of_items_to_buy
        christmas_spirit +=17
    if i == days_until_christmas:
        christmas_spirit -= 20
        money_spent+= 23 * number_of_items_to_buy
    if i % 11==0:
        number_of_items_to_buy +=2


print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")