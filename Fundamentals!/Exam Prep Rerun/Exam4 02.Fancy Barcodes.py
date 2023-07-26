import re

pattern = r"@\#{1,}([A-Z][A-Za-z0-9]{4,}[A-Z])@\#{1,}"

text = ""
n = int(input())
for i in range(n):
    bar = input()
    matches =re.findall(pattern,bar)
    if not matches:
        print("Invalid barcode")
        continue
    digits = r"[\d+]"
    score = re.findall(digits,bar)
    if not score:
        score = "00"
        print(f"Product group: {score}")
    else:
        print(f"Product group: {''.join(score)}")

