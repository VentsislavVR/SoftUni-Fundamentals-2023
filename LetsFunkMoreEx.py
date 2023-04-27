#1st
# def data_type_check(c,n):
#     result = ""
#     if c == "int":
#         result = int(n) * 2
#     elif c == "real":
#         result = f'{float(n) * 1.50:.2f}'
#     elif c == "string":
#         result= f'${n}$'
#     return result
#
#
# comand = input()
# num_or_str= input()
# print(data_type_check(comand,num_or_str))

#2nd
def deba_shibani_afasfsf(first,second,third,fourth):
    x = []
    y = []

    for n in (first,second,third,fourth):
        if abs(first) > abs(third):
            x.append(third)
        else:
            x.append(first)
        if abs(second) > abs(fourth):
            x.append(third)
        else:
            x.append(first)
    # closest_x = min(x,key=abs())
    # closest_y = min(y,key=abs())

    return f"({x}, {y})"


X1 = input()
Y1 = input()
X2 = input()
Y2 = input()
print(deba_shibani_afasfsf(X1,Y1,X2,Y2))

