def find_idx(seq, element, target_count):
    count = 0
    for idx in range(len(seq)):
        if seq[idx] == element:
            count += 1
            if count == target_count:
                return idx
    return "Nope"


my_list = input().split()
my_element = input()
my_target = int(input())
print(find_idx(my_list, my_element, my_target))
