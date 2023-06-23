chars = input().split(", ")

result = {char:ord(char) for char in chars}
print(result)