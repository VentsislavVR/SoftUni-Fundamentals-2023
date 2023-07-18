input_list = input().split()

occurrences = {num: input_list.count(num) for num in input_list}

for number,count in occurrences.items():
    print(f"{float(number)} - {count} times")