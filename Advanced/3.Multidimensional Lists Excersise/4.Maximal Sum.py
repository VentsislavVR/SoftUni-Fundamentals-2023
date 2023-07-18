rows, cols = [int(x) for x in input().split()]

matrix = [[int(j) for j in input().split()] for i in range(rows)]
best_sum_nums = []
max_sum = float("-inf")
for i in range(rows):
    for j in range(cols):
        if i >= rows -2 or j >= cols -2:
            break
        top_left = matrix[i][j]
        top_centre = matrix[i][j+1]
        top_right = matrix[i][j+2]
        middle_left = matrix[i+1][j]
        middle_centre = matrix[i+1][j+1]
        middle_right = matrix[i+1][j+2]
        bottom_left = matrix[i+2][j]
        bottom_centre = matrix[i+2][j+1]
        bottom_right = matrix[i+2][j+2]
        current_best = top_right + top_centre + top_left + middle_right\
                       +middle_centre+middle_left+\
                       bottom_centre+bottom_left+bottom_right
        if current_best > max_sum:
            best_sum_nums.clear()
            best_sum_nums.extend([top_left,top_centre,top_right,
                                  middle_left,middle_centre,middle_right,
                                  bottom_left,bottom_centre,bottom_right])
            max_sum = current_best
print(f"Sum = {max_sum}")
for i in range(len(best_sum_nums)):
    print(best_sum_nums[i], end=" ")
    if (i + 1) % 3 == 0:
        print()
# [1, 5, 5, 2, 4],
# [2, 1, 4, 14, 3],
# [3, 7, 11, 2, 8],
# [4, 8, 12, 16, 4]
