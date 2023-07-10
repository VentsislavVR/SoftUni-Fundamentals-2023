import re

data = input()
emojis = re.findall(r"(\:{2}|\*{2})([A-Z][a-z]{2,})\1", data)
cool_threshold = 1
cool_emojis = []

for char in data:
    if char.isdigit():
        cool_threshold *= int(char)

for emoji in emojis:
    coolness = sum(ord(ch) for ch in emoji[1])
    if coolness >= cool_threshold:
        cool_emojis.append(emoji[0] + emoji[1] + emoji[0])

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
