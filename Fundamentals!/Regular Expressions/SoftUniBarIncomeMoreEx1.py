import re
total_price = 0
customers = []
while True:
    line = input()
    if line == "end of shift":
        break
    pattern = r"%(?P<name>[A-Z][a-z]+)%[^\.\$\%\|]*?" \
              r"<(?P<item>\w+)>[^\.\%\$\|]*?\|(?P<count>\d+)\|[^\.\%\$\|]*?(?P<price>\d+\.?\d*)\$"
    match = re.match(pattern,line)
    if not match:
        continue
    groups = match.groupdict()
    for items in groups:
        total_price += float(groups["price"]) * int(groups["count"])
        print(f"{groups['name']}: {groups['item']} - {float(groups['count']) * float(groups['price']):.2f}")
        break
print(f"Total income: {total_price:.2f}")