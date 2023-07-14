from collections import defaultdict

data = input()

result = {}
for char in data:
    for ch in char:
        if ch not in result:
            result[ch] = 0
        result[ch] += 1

for key,value in sorted(result.items()):
    print(f"{key}: {value} time/s")
