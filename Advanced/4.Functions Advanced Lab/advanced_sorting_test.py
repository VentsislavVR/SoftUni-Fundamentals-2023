# my_dict = {"Peter": 21, "George": 18, "John": 45}
#
# print(sorted(my_dict.items(),key=lambda x:x[1],reverse=True))

my_dict = {"Peter": [2, 6], "George": [4], "John": [6, 3]}

print(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))  # - means descending used instead of reversed True
# sorting by grades descending then my name
