def check_idx_func(row, col):
    return 0 <= row < rows and 0 <= col < rows


def add_func(info):
    row, col, value = info
    if check_idx_func(row, col):
        matrix[row][col] += value
    else:
        print("Invalid coordinates")


def subtract_func(info):
    row, col, value = info
    if check_idx_func(row, col):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")


rows = int(input())

matrix = [[int(el) for el in input().split()] for i in range(rows)]

while True:
    command, *info = input().split()
    if command == "END":
        break
    info = [int(x) if x.replace("-", "").isdigit() else x for x in info] # isdigit takes only positive values
    if command == "Add":
        add_func(info)
    elif command == "Subtract":
        subtract_func(info)

[print(*row, sep=" ") for row in matrix]