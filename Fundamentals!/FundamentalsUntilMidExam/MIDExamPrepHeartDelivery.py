# neighborhood = [int(x) for x in input().split("@")]
# cupid_last = 0
#
# while True:
#     command = input()
#     if command == "Love!":
#         break
#     current = command.split(" ")
#     jump = int(current[1])
#     if jump >= len(neighborhood):
#         jump = 0
#     current_jump = jump
#     if neighborhood[jump] == 0:
#         print(f"Place {jump} has Valentine's day.")
#     if neighborhood[jump] <= 0:
#         print(f"Place {jump} already had Valentine's day.")
#
#     neighborhood[jump] -= 2
#     jump += current_jump
#     cupid_last = jump - 1
# print(f"Cupid's last position was {cupid_last}.")
# if all(place == 0 for place in neighborhood):
#     print("Mission was successful.")
# else:
#     failed_houses = len([place for place in neighborhood if place > 0])
#     print(f"Cupid has failed {failed_houses} places.")
#  MIIINE
# neighborhood = [int(x) for x in input().split("@")]
#
# while True:
#     command = input()
#     if command == "Love!":
#         break
#     current = command.split(" ")
#     jump = int(current[1])
#     for j in neighborhood:
#         neighborhood[jump] -= 2
#         if jump > len(neighborhood):
#             jump = len(neighborhood) - jump
#         if neighborhood[jump] == 0:
#             print(f"Place {neighborhood[jump]} has Valentine's day.")
#         # jump += 2
#         break
# print(neighborhood)
# neighborhood = [int(x) for x in input().split("@")]
# command = input()
#
# while True:
#     command = input()
#     if command == "Love!":
#         break
#     current_command = command.split()
#     jump = int(current_command[1])
#     for j in neighborhood:
#         neighborhood[jump] -=2
#         if neighborhood[jump] == 0:
#             print(f"Place {neighborhood[jump]} has Valentine's day.")

