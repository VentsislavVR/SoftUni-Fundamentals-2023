targets = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {len([x for x in targets if x == -1])} -> {' '.join(map(str,targets))}")
        break
    index = int(command)
    if index in range(len(targets)):
        current_shot = targets[index]
        targets[index] = -1
        for idx,i in enumerate(targets):
            if i > current_shot:
                targets[idx] -= current_shot
                continue
            elif i <= current_shot and i != -1:
                targets[idx] += current_shot





