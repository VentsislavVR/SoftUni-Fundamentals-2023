master = input().split(", ")

positive_list = [int(x) for x in master if int(x) >= 0]
negatie_list = [int(y) for y in master if int(y) < 0]
even_list = [int(z) for z in master if int(z) % 2 == 0]
odd_list = [int(h) for h in master if int(h) % 2 != 0]


print(f"Positive: {', '.join((map(str,positive_list)))}")
print(f"Negative: {', '.join((map(str,negatie_list)))}")
print(f"Even: {', '.join((map(str,even_list)))}")
print(f"Odd: {', '.join(map(str,odd_list))}")
