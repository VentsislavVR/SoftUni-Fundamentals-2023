# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
data = input().upper()
final_rage_quit = ""
for index in range(len(data)):
    if data[index].isdigit():
        if len(final_rage_quit) < 1:
            final_rage_quit = data[index-1] * int(data[index])
        else:
            final_rage_quit = data[:index] *int(data[index])
    else:
        final_rage_quit += data[index]



print(final_rage_quit)

