#1.2 set slower
text = input()

for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")


#1.1 dict a bit faster
# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
# for letter , times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")


# 1.0
# data = input()
#
# result = {}
# for char in data:
#     for ch in char:
#         if ch not in result:
#             result[ch] = 0
#         result[ch] += 1
#
# for key,value in sorted(result.items()):
#     print(f"{key}: {value} time/s")
