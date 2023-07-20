
rows = int(input())

matrix = [[int(el) for el in input().split()]for row in range(rows)]


primary_diagonal =[matrix[j][j] for j in range(rows)]
secondary_diagonal = [matrix[j][rows - 1 - j] for j in range(rows)]

result = sum(primary_diagonal)-sum(secondary_diagonal)
print(abs(result))

