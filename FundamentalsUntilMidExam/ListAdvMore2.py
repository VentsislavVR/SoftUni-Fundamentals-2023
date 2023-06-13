update = [int(x) for x in input().split(".")]

if update[2] >= 9:
    update[2] = 0
    if update[1] >= 9:
        update[1] = 0
        update[0] += 1
    else:
        update[1] += 1
else:
    update[2] += 1

result = [str(y) for y in update]
print(".".join(result))

