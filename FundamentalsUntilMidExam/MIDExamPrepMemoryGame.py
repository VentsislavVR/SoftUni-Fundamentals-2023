def is_index_in_range(index, cards_count):
    if 0 <= index < cards_count:
        return True
    return False


def check_indexes_are_valid(index1, index2, count_cards):
    if is_index_in_range(index1, count_cards) \
            and is_index_in_range(index2, count_cards) \
            and index1 != index2:
        return True
    return False


cards = input().split()

command = input()
n_moves = 0
while command != "end":
    n_moves += 1
    index1, index2 = [int(el) for el in command.split()]
    if check_indexes_are_valid(index1, index2, len(cards)):
        if cards[index1] == cards[index2]:
            element = cards[index1]
            cards.pop(index1)
            cards.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print(f"Try again!")
    else:
        element_to_add = f"-{n_moves}a"
        index = len(cards) // 2
        cards.insert(index, element_to_add)
        cards.insert(index, element_to_add)
        print("Invalid input! Adding additional elements to the board")
    if not cards:
        print(f"You have won in {n_moves} turns!")
        exit(0)
    command = input()
print(f"Sorry you lose :(")
print(*cards, sep=" ")
