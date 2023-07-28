from math import log

number = int(input())
base = input()

if base == "natural":
    print(f"{log(number):.2f}")
else:
    base = int(base)
    print(f"{log(10,base):.2f}")