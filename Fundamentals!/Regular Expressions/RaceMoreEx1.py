import re

text = input()
racers ={}
while True:
    info = input()
    if info == "end of race":
        break
    name = re.findall(r'[A-Za-z]+', info)
    key = "".join(name)
    digits = re.findall(r'\d', info)  # Find all digits using \d pattern
    digits = [int(x) for x in digits]  # Convert digits to integers
    value = sum(digits)
    if key in racers:
        racers[key]+=value
        continue
    if key in text:
        racers[key] = value

# winners =list(dict(sorted(racers.items(), key=lambda x: x[1],reverse=True)))
# print(f"1st place: {winners[0]}")
# print(f"2nd place: {winners[1]}")
# print(f"3rd place: {winners[2]}")
winners = sorted(racers.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {winners[0][0]}")
print(f"2nd place: {winners[1][0]}")
print(f"3rd place: {winners[2][0]}")


