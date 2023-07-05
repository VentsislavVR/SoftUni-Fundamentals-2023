#first
# data = input().split()
# result = [int(num)* -1 for num in data]
# print(result)
#second
# factor = int(input())
# count = int(input())
# result = []
# for num in range(1,count+1):
#     result.append(num*factor)
# print(result)

# teamA = []
# teamB = []
# for teams in range(1,12):
#     teamA.append(f"A-{teams}")
#     teamB.append(f"B-{teams}")
#
# recived_cards = input().split()
# terminated = False
# for card in range(len(recived_cards)):
#     if recived_cards[card] in teamA:
#         teamA.remove(recived_cards[card])
#     if recived_cards[card] in teamB:
#         teamB.remove(recived_cards[card])
#     if len(teamA) < 7 or len(teamB) < 0:
#         print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
#         print("Game was terminated")
#         terminated = True
#         break
#
# if terminated== False:
#     print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")

# coins = input().split(", ")
# beggars = int(input())
# beggars_list =[0] * beggars
# for i in range(len(coins)):
#     coin = int(coins[i])
#     beggar_index = i % beggars
#     beggars_list[beggar_index] += coin
#
# print(beggars_list)

# cards = input().split()
#
# counter = int(input())
# for _ in range(counter):
#     first_half = []
#     second_half = []
#     for idx in range(1, len(cards) - 1):
#         if idx < len(cards) // 2:
#             first_half.append(cards[idx])
#         else:
#             second_half.append(cards[idx])
#
#     shuffled = []
#     first_idx = 0
#     second_idx = 0
#     for idx in range(len(first_half) * 2):
#         if idx % 2 == 0:
#             shuffled.append(second_half[second_idx])
#             second_idx += 1
#         else:
#             shuffled.append(first_half[first_idx])
#             first_idx += 1
#
#     cards = [cards[0]] + shuffled + [cards[-1]]
# print(cards)

data = [int(x) for x in input().split()]

to_remove = int(input())

# data.sort(reverse=True)

for i in range(len(data)):
    if i < len(data) / sum(data):
        data.remove(i)
        data.insert(i,-1)
        data.pop(-1)

print(data)