# 1.0 EZ
first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    if command == "Add First":
        [first.add(int(el)) for el in data]
    elif command == "Add Second":
        [second.add(int(el)) for el in data]
    elif command == "Remove First":
        [first.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [second.discard(int(el)) for el in data]
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
