import re
text = input()

matches = re.findall(r"\b_([A-Za-z\d]+)\b",text)

print(",".join(matches))