#1.1
table = set()
for _ in range(int(input())):
    for el in input().split():
        table.add(el)
print(*table, sep="\n")

#1.0
# n = int(input())
# chemicals = set()
#
# for chemi in range(n):
#     element = input().split()
#     for el in element:
#         chemicals.add(el)
# for e in chemicals:
#     print(e)
