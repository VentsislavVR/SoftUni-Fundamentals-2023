def find_elemwnt_in_matrix(matrix, element):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):  # or range(i)
            if matrix[i][j] == element:
                return (i, j)


rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

searched_symbol = input()
position = find_elemwnt_in_matrix(matrix, searched_symbol)

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
