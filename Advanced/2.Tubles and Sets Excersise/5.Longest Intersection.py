#revised
# n = int(input())

# final_max = set()
# for i in range(n):
#     intersection = input().split("-")
#     first = intersection[0]
#     second = intersection[1]
#     fstart = first.split(",")
#     sstart = second.split(',')
#     first_start = int(fstart[0])
#     first_end = int(fstart[1])
#     second_start = int(sstart[0])
#     second_end = int(sstart[1])
#
#     first_set = set(range(first_start, first_end + 1))
#     second_set = set(range(second_start, second_end + 1))
#
#     current_max = first_set.intersection(second_set)
#
#     if len(current_max) > len(final_max):
#         final_max = current_max
#
# print(f"Longest intersection is [{', '.join(str(x) for x in final_max)}] with length {len(final_max)}")

# bad max logic

# n = int(input())
#
# finall_max = set()
# current_max = set()
# for i in range(n):
#     first_set = set()
#     secon_set = set()
#     intersection = input().split("-")
#     first = intersection[0]
#     second = intersection[1]
#     fstart = first.split(",")
#     sstart = second.split(',')
#     first_start = int(fstart[0])
#     first_end = int(fstart[1])
#     second_start = int(sstart[0])
#     second_end = int(sstart[1])
#     for x in range(first_start, first_end + 1):
#         first_set.add(x)
#     for y in range(second_start, second_end + 1):
#         secon_set.add(y)
#     current_max = first_set.intersection(secon_set)
#
#     if len(current_max) > len(finall_max):
#         current_max = first_set.intersection(secon_set)
#         finall_max = current_max
#     else:
#         finall_max = first_set.intersection(secon_set)
# print(f"Longest intersection is [{', '.join(str(x) for x in finall_max)}] with length {len(finall_max)}")
