import re

text = input()
total_calories = 0
matches= re.findall(r"([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1",text)
products = []
for match in matches:
    product = match[1]
    expiration_date = match[2]
    calories = int(match[3])

    products.append(f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}")
    total_calories += calories

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
print("\n".join(products))