message = input()
final = ""
for ch in message:
    new= chr(ord(ch)+3)
    final +=new

print(final)