n = int(input())
chemicals = set()

for chemi in range(n):
    element = input().split()
    for el in element:
        chemicals.add(el)
for e in chemicals:
    print(e)
