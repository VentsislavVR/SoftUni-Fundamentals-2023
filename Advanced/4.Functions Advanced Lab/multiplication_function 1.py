def multiply(*data):
    result = data[0] * data[1] * data[2]
    return result
data = 1,4,5
print(multiply(*data))
