# 1st
# def remove_vowels_from_text(text):
#     forbidden_letters = ['a', 'o', 'u', 'e', 'i']
#     result = [char for char in text if char.lower() not in forbidden_letters]
#     return "".join(result)
#
#
# text = input()
# print(remove_vowels_from_text(text))
#2nd
n_wagons = int(input())
train = [0] * n_wagons
commands = input()

while commands != "End":
    action = commands.split()[0]
    if action == "add":
        n_people = int(commands.split()[1])
        train[-1] += n_people
    elif action == "insert":
        index = int(commands.split()[1])
        n_people = int(commands.split()[2])
        train[index] += n_people
    elif action == "leave":
        index = int(commands.split()[1])
        n_people = int(commands.split()[2])
        train[index] -= n_people

    commands = input()
print(train)
=======
nums = [ num for num in range(1,11) if num % 2 == 0]
print(nums)
>>>>>>> origin/main

