# 72olle 103doo 100ya
# You are given a secret message you should decipher. To do that, you need to know that in each word:
# • the second and the last letter are switched (e.g., Holle means Hello)
# • the first letter is replaced by its character code (e.g., 72 means H)

message = input().split(' ')
deciphered = []

for word in message:
    ascii_char = [char for char in word if char.isdigit()]
    word_list = [char for char in word if char not in ascii_char]

    first_letter = chr(int(''.join(ascii_char)))
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    new_word = first_letter + ''.join(word_list)
    deciphered.append(new_word)

print(' '.join(deciphered))




