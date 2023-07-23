import re

pattern = r"(?P<item>#[A-Za-z\s]+#|\|\w+\|)(?P<exp>\d{2}\/\d{2}\/\d{2})(?P<cal>#\d+#|\|\d+\|)"

text = input()

matches = re.finditer(pattern, text)
total_cal = 0
food_items = []

for match in matches:
    product_name = match.group("item")[1:-1]
    expiration_date = match.group("exp")
    calories = int(match.group("cal")[1:-1])
    total_cal += calories

    food_items.append((product_name, expiration_date, calories))

print(f"You have food to last you for: {total_cal // 2000} days!")

for item in food_items:
    product_name, expiration_date, calories = item
    print(f"Item: {product_name}, Best before: {expiration_date}, Nutrition: {calories}")
