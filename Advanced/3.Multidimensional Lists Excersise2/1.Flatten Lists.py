data = input()

matrix = [[int(x) for x in row.strip().split()] for row in data.split('|')]
flattened_matrix = [str(cell) for row in matrix[::-1] for cell in row]
result = ' '.join(flattened_matrix)

print(result)