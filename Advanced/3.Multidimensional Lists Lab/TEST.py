# p_and_l = [
#     [300, 200, 400],# row 0
#     [200, 200, 100],# row 1
#     [450, 200, 80] ,# row 2
#   #col 0 col 1  col 2
# ]
#
# print(p_and_l[1][0])
#################################
#FLAT 1
# matrix = [[1,2,3],[4,5,6]]
# flatten = []
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         current_element = matrix[row_index][col_index]
#         flatten.append(current_element)
# print(flatten)
#################################

#################################
# FLATTEN 2 better option
# matrix = [[1,2,3],[4,5,6]]
# flatten = []
# for el in matrix:
#     flatten.extend(el)
# print(flatten)

# FLATTEN 3
################################# !!!
# matrix = [[1,2,3],[4,5,6]]
# flatten = [el for list_el in matrix for el in list_el]
# print(flatten)
###########################################

matrix = [[1,2,3],[4,5,6]]
# [print(inner_list) for inner_list matrix] # prints inner lists
# use print(*inner_list) to get rid of []

#or
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
       print(matrix[row_index][col_index],end=" ")
    print()