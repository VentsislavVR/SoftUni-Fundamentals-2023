rows = int(input())

matrix = [[int(el) for el in input().split(",")]for r in range(rows)]

flatten = []
for i in matrix:
    flatten.extend(i)
print(flatten)

# hard way
# row = int(input())
# matrix = []
# flatten = []
# for _ in range(row):
#     inner_list = [int(el) for el in input().split(",")]
#     matrix.append(inner_list)
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         flatten.append(matrix[row_index][col_index])
#
# print(flatten)