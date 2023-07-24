def age_assignment(*args,**kwargs):
    result = []
    for key,value in kwargs.items():
        for n in args:
            if key in n[0]: # or n.startswith(key)
                result.append(f"{n} is {value} years old.")
                break
    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36,
A=22, B=61))
