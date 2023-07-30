import re

pattern = r"\|([A-Z]{4,})\|:#([A-z]+\s{1}[A-z]+)#"

n = int(input())

for i in range(n):
    boss = input()
    matches = re.findall(pattern,boss)

    if not matches:
        print("Access denied!")
    else:
        print(f"{matches[0][0]}, The {matches[0][1]}")
        print(f">> Strength: {len(matches[0][0])}")
        print(f">> Armor: {len(matches[0][1])}")


