first = input().split(", ")
second = input().split(", ")


best = []
for fi in first:
    for sec in second:
        if fi in sec:
            best.append(fi)
            break
print(best)