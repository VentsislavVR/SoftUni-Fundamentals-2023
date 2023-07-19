
#                                                          [['0', 'K', '0', 'K', '0'],
#                                                          ['K', '0', '0', '0', 'K'],
#                                                          ['0', '0', 'K', '0', '0'],
#                                                          ['K', '0', '0', '0', 'K'],
#                                                          ['0', 'K', '0', 'K', '0']]
rows = int(input())
matrix = [[el for el in input()] for y in range(rows)]
knights_on_board = []

for row in range(rows):
    for col in range(len(matrix[row])):  # Calculate the number of columns based on the current row.
        if matrix[row][col] == "K":
            knights_on_board.append((row, col))
