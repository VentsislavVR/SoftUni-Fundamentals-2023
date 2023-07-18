row,cols = [int(el) for el in input().split()]

matrix = [[j for j in input().split()] for i in range(row)]

matching = 0
for i in range(row-1):
    for j in range(cols-1):
        current_element = matrix[i][j]
        bottom = matrix[i+1][j]
        right = matrix[i][j+1]
        diagonal = matrix[i+1][j+1]

        if current_element == bottom == right == diagonal:
            matching += 1
print(matching)

#[['A','B','B','D'],
# ['E','B','B','B'],
# ['I', J','B','B']]