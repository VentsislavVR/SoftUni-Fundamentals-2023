rows,cols = [int(el) for el in input().split(", ")]

# matrix = [[int(el) for el in input().split()] for col in range(rows)]
matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

for col_index in range(cols):
    sum_col_elements = 0
    for row_index in range(rows):
        sum_col_elements += matrix[row_index][col_index]
    print(sum_col_elements)