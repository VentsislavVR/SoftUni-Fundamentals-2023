# data = input()
#
# matrix = [[int(x) for x in row.strip().split()] for row in data.split('|')]
# flattened_matrix = [str(cell) for row in matrix[::-1] for cell in row]
# result = ' '.join(flattened_matrix)
#
# print(result)

##############################
# Diyan 1.0 easier than the top (my version)

line = input().split("|")
sub_list = []
for sub_string in line[::-1]:
    sub_list.extend(sub_string.split())
print(*sub_list)
# Diyan 1.1 ## wil crash if input has 2 x "|" if the if statement is not added at the end

# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(sub_list)for sub_list in numbers[::-1] if sub_list])