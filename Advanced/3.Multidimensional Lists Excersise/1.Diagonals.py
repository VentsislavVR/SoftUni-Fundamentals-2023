# rows = int(input())
#
# matrix = [
#
# ]
# first_diagonal = []
# second_diagonal = []
# for idx in range(rows)[::-1]:
#     inner_list = [int(el) for el in input().split(", ")]
#     matrix.append(inner_list)
#     first_diagonal.append(inner_list[idx])
# for j in range(rows):
#     second_diagonal.append(matrix[j][j])
#
#
# print(f"Primary diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {sum(second_diagonal)}")
# print(f"Secondary diagonal: {', '.join(str(x)for x in first_diagonal)}. Sum: {sum(first_diagonal)}")

rows = int(input())
matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

primary_diagonal = [matrix[j][j] for j in range(rows)]
secondary_diagonal = [matrix[j][rows - 1 - j] for j in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")