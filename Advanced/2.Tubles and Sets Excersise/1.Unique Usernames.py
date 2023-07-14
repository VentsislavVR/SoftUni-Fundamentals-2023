num = int(input())

usernames= set()

for i in range(num):
    names = input()
    usernames.add(names)
for name in usernames:
    print(name)
