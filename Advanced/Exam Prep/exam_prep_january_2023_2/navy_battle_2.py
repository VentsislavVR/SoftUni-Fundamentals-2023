size = int(input())

cruisers = 3
bombs_hit = 0

matrix = []
submarine_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = list(input())
    matrix.append(line)

    if "S" in line:
        submarine_pos = [row, line.index("S")]
        matrix[submarine_pos[0]][submarine_pos[1]] = "-"

while cruisers:
    direction = input()

    submarine_pos += directions[direction]

    r = directions[direction][0] + submarine_pos[0]
    c = directions[direction][1] + submarine_pos[1]

    submarine_pos = [r, c]
    if matrix[r][c] == "C":
        cruisers -= 1

    elif matrix[r][c] == "*":
        bombs_hit += 1

        if bombs_hit == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            break

    matrix[r][c] = "-"

else:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

matrix[submarine_pos[0]][submarine_pos[1]] = "S"
[print(''.join(row)) for row in matrix]
print()
[print(*row,sep="") for row in matrix]