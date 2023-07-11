# from collections import deque
# ROTATION OF QUE
# name_of_players = input().split(" ")
# step_of_hot_potato = int(input())
#
# players_deque = deque(name_of_players)
# counter = 0
#
# while len(players_deque) > 1:
#     counter += 1
#     current_name_of_player = players_deque.popleft()
#     if counter == step_of_hot_potato:
#         print(f"Removed {current_name_of_player}")
#         counter = 0
#     else:
#         players_deque.append(current_name_of_player)
# print(f"Last is {players_deque[0]}")

from collections import deque
# using step instead of a counter
name_of_players = input().split(" ")
step_of_hot_potato = int(input())

players_deque = deque(name_of_players)


while len(players_deque) > 1:
    for _ in range(step_of_hot_potato-1):
        players_deque.append(players_deque.popleft())
    print(f"Removed {players_deque.popleft()}")

print(f"Last is {players_deque.pop()}")