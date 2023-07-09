import re
data = input()
pattern = r"([@|\#])([A-Za-z]{3,})\1{2,2}([A-Za-z]{3,})\1"

matches = re.finditer(pattern,data)
found = {}
for pairs in matches:
    current_pair = re.split("@|\#", pairs.group())
    word_one = current_pair[1]
    second_word = current_pair[3]
    found[word_one] = second_word

result = []
if found:
    print(f"{len(found)} word pairs found!")
else:
    print("No word pairs found!")
for key,value in found.items():
    if key == value[::-1]:
        result.append(f"{key} <=> {value}")
if result:
    print("The mirror words are:")
    print(", ".join(result))
else:
    print("No mirror words!")

