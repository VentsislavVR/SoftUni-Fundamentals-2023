import re

regex = r"([#|@])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

test_str = input()

matches = re.finditer(regex, test_str)
mirror_word = []
all_matched = 0
for match in matches:
    first = match.group(2)
    second = match.group(3)
    all_matched +=1
    if first == second[::-1]:
        mirror_word.append(f"{first} <=> {second}")

if all_matched <= 0:
    print("No word pairs found!")
else:
    print(f"{all_matched} word pairs found!")
if not mirror_word:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_word))