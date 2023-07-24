import re

pattern = r"([=|\/])([A-Z][A-Za-z]{2,})\1"

text = input()

points = 0

match = re.findall(pattern,text)
resul = []

for m in match:
    resul.append(m[1])
    points += len(m[1])

print(f"Destinations: {', '.join(resul)}")
print(f"Travel Points: {points}")