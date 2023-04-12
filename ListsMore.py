numbers=input().split(",")

new_list = []
for zero in numbers:
    if int(zero) == 0:
        numbers.remove(zero)
        numbers.append(zero)
for chisla in numbers:
    new_list.append(int(chisla))
print(new_list)

