from itertools import islice

def calculate_sum(submatrix):
    return sum(sum(row) for row in submatrix)

def find_max_submatrix(matrix):
    max_sum = float("-inf")
    max_submatrix = None

    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            submatrix = list(islice((row[j:j+3] for row in matrix[i:i+3]), 3))
            current_sum = calculate_sum(submatrix)
            if current_sum > max_sum:
                max_sum = current_sum
                max_submatrix = submatrix

    return max_submatrix, max_sum

def print_submatrix(matrix):
    for row in matrix:
        print(' '.join(str(element) for element in row))

rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

max_submatrix, max_sum = find_max_submatrix(matrix)

print(f"Sum = {max_sum}")
print_submatrix(max_submatrix)
