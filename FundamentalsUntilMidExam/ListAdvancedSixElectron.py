num_electrons = int(input())

filled_shells = []
shell_num = 1
while num_electrons > 0:
    max_electrons = 2 * shell_num ** 2
    if num_electrons >= max_electrons:
        filled_shells.append(max_electrons)
        num_electrons -= max_electrons
    else:
        filled_shells.append(num_electrons)
        break
    shell_num += 1

print(filled_shells)

