# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
data = input().upper()
final_rage_quit = ""
current = ""
for index in range(len(data)):
    current += final_rage_quit
    if data[index].isdigit():
        current *= int(data[index])

    else:
        final_rage_quit += current
        current = ""



print(final_rage_quit)

