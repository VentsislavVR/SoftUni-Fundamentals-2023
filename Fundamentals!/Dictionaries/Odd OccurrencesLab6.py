# word_keys = [el for el in input().lower().split(" ")]
#
# result_dict = {}
# for element in word_keys:
#     key = element
#     value_start = 0
#     if element not in result_dict:
#         key = element
#         result_dict[key] = value_start
#         result_dict[key] += 1
#     else:
#         result_dict[key] +=1
#
# for key,value in result_dict.items():
#     if value % 2 !=0:
#         print(key,end=" ")
# words_keys = [el.lower() for el in input().split()]
# default = 0
# occurrences = dict.fromkeys(words_keys,default)
#
# for word in words_keys:
#     occurrences[word] += 1
# for word, count in occurrences.items():
#     if count % 2 != 0:
#         print(word, end=" ")