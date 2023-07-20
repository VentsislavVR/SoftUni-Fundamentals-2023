n = int(input())

matrix = [[int(x) for x in input().split()] for i in range(n)] # initial matrix
coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split()) # bombs locations

directions = ( # location of elements which will take damage from the bomb
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1), # left
    (-1, 1), # top-right
    (-1,-1), # top-left
    (1, -1),  # bottom-left
    (1, 1),   # bottom-right
    (0, 0), # current (this should be last
)

for row, col in coordinates: # iterating over the bombs
    if matrix[row][col] <= 0:
        continue
    for x, y in directions: # the impact of the bomb
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n: # current idx greater than 0 and less than matrix boarders
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0 # dealing damage


alive_cells = [num for row in range(n) for num in matrix[row] if num >0] # only positive elements

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*matrix[r],sep=" ") for r in range(n)]