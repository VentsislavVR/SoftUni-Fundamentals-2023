
## 1st
rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

searched_symbol = input()
position = None

for i in range(rows):
    if position:
        break
    for j in range(len(matrix[i])): # or range(i)
        if matrix[i][j] == searched_symbol:
            position = (i,j)
            break
if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
