rows = int(input())

matrix = [

]
sum = 0
for idx in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)
    sum+= inner_list[idx]
print(sum)
#########  OR  ################
# sum_diagonal = 0
# for index in range(rows):
#     sum_diagonal += matrix[index][index]
# print(sum_diagonal)