import re
text = input().lower()
target = input().lower()

matches = re.findall(rf"\b{target}\b", text)

print(len(matches))