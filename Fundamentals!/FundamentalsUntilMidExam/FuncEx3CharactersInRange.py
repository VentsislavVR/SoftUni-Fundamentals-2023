def all_the_characters(first,second):
    characters = []
    for ch in range(ord(first)+1,ord(second)):
        characters.append(chr(ch))
    return characters

first_character = input()
second_character = input()
result = all_the_characters(first_character,second_character)
print(*result)