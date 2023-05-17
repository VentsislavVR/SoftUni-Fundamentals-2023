words = input().split()
searched_palindrome = input()

print([word for word in words if word == word[::-1]])
print(words.count(searched_palindrome))


