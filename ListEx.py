#   FIRST
# input_elements = input().split()
#
# result = []
#
# for el in input_elements:
#     number = int(el)
#     result.append(-number)
# print(result)

#  SECOND
# factor = int(input())
# count = int(input())
#
# result = []
# for num in range(1,count+1):
#     result.append(num*factor)
#
# print(result)
#  THIRD

# cards = input().split()
#
# first_team_sent_off_players = []
# second_team_sent_off_players = []
#
# should_terminate = False
#
# for card in cards:
#     if card in first_team_sent_off_players or card in second_team_sent_off_players:
#         continue
#
#     card_args = card.split("-")
#     team_name = card_args[0]
#     player_number = card_args[1]
#
#     is_first_team = team_name == "A"
#     if is_first_team:
#         first_team_sent_off_players.append(card)
#     else:
#         second_team_sent_off_players.append(card)
#     if len(first_team_sent_off_players) > 4 or len(second_team_sent_off_players) > 4:
#         should_terminate = True
#         break
# initial_player_count = 11
# print(f"Team A - {initial_player_count-len(first_team_sent_off_players)}; Team B - {initial_player_count-len(second_team_sent_off_players)}")
#
# if should_terminate:
#     print("Game was terminated")
# # FOURTH !!!!
#
# numbers = input().split(", ")
# beggars_count = int(input())
#
# beggars = [0] * beggars_count
#
# for idx in range(len(numbers)):
#     beggar_idx = idx % beggars_count
#     num = int(numbers[idx])
#     beggars[beggar_idx] += num
#
# print(beggars)
# FIFTH !!!!!
cards = input().split()
counter = int(input())
for _ in range(counter):
    first_half = []
    second_half = []
    for idx in range(1,len(cards)-1):
        card = cards[idx]
        if idx < len(cards) / 2:
            first_half.append(card)
        else:
            second_half.append(card)
    shuffled = []
    first_part_idx = 0
    second_part_idx = 0
    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            shuffled.append(second_half[second_part_idx])
            second_part_idx += 1
        else:
            shuffled.append(first_half[first_part_idx])
            first_part_idx += 1

    cards = [cards[0]] + shuffled + [cards[-1]]
print(cards)











