# 1.2
longest_intersection = set()
for _ in range(int(input())):
    first_data,second_data = [el.split(",") for el in input().split("-")] # "3,4" - 1,2 => [ "3" , "4"]

    first_range = set(range(int(first_data[0]),int(first_data[1])+1))
    second_range = set(range(int(second_data[0]),int(second_data[1])+1))
    intesection = first_range.intersection(second_range)
    if len(intesection) > len(longest_intersection):
        longest_intersection = intesection
print(f"Longest intersection is "
      f"[{', '.join(str(x)for x in longest_intersection)}] "
      f"with length {len(longest_intersection)}")

#revised
# n = int(input())
#
# final_max = set()
# for i in range(n):
#     intersection = input().split("-")
#     first, second = intersection[0], intersection[1]
#     fstart, sstart = first.split(","), second.split(',')
#     first_start, first_end = int(fstart[0]), int(fstart[1])
#     second_start, second_end = int(sstart[0]), int(sstart[1])
#
#     first_set = set(range(first_start, first_end + 1))
#     second_set = set(range(second_start, second_end + 1))
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
