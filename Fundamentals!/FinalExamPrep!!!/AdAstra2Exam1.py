import re
from math import floor

text = input()

calories_per_day = 2000
total= 0
items = re.findall(r"([?:\||#])+(?P<item>[A-Za-z\s]+)\1(?P<exp>\d{2}/\d{2}/\d{2})\1(?P<cal>[0-9]{1,4})",text)
if items:

    for cal in items:
        if int(cal[3]) <= 10000:
         total += int(cal[3])
days_until_almost_instant_death= floor(total//calories_per_day)
print(f"You have food to last you for: {days_until_almost_instant_death} days!")

if days_until_almost_instant_death >0:
    for cal in items:
        if int(cal[3]) <= 10000:
            print(f"Item: {cal[1]}, Best before: {cal[2]}, Nutrition: {cal[3]}")

