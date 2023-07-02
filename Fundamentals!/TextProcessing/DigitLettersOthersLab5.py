data = input()
digits , letters,others = [],[],[]


for ch in data:
    if ch.isdigit():
        digits.append(ch)
    elif ch.isalpha():
        letters.append(ch)
    else:
        others.append(ch)
print(*digits,sep="")
print(*letters,sep="")
print(*others,sep="")
