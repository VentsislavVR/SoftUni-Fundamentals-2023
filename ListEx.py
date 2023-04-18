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
# print(f"Team A - {initial_player_count-len(first_team_sent_off_players)};
# Team B - {initial_player_count-len(second_team_sent_off_players)}")
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
# cards = input().split()
# counter = int(input())
# for _ in range(counter):
#     first_half = []
#     second_half = []
#     for idx in range(1,len(cards)-1):
#         card = cards[idx]
#         if idx < len(cards) / 2:
#             first_half.append(card)
#         else:
#             second_half.append(card)
#     shuffled = []
#     first_part_idx = 0
#     second_part_idx = 0
#     for idx in range(len(first_half) * 2):
#         if idx % 2 == 0:
#             shuffled.append(second_half[second_part_idx])
#             second_part_idx += 1
#         else:
#             shuffled.append(first_half[first_part_idx])
#             first_part_idx += 1
#
#     cards = [cards[0]] + shuffled + [cards[-1]]
# print(cards)
# SIXTH
# numbers = [int(x) for x in input().split()]
# count = int(input())
# for _ in range(count):
#     min_number = min(numbers)
#     numbers.remove(min_number)
# print(', '.join([str(x) for x in numbers]))

# EIGHT

# cells = input().split("#")
# water = int(input())
#
# processed_cells = []
# total_fire = 0
#
# for cell in cells:
#     cell_args = cell.split(" = ")
#     level = cell_args[0]
#     value = int(cell_args[1])
#     if level == "High" and (value < 81 or value > 125):
#         continue
#     if level == "Medium" and (value < 51 or value > 80):
#         continue
#     if level == "Low" and (value < 1 or value > 50):
#         continue
#
#     if value > water:
#         continue
#     water -= value
#     total_fire += value
#     processed_cells.append(value)
#
# print("Cells:")
# for cell in processed_cells:
#     print(f" - {cell}")
# effort = total_fire * 0.25
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")
# SEVENTH

# gifts = input().split()
#
# while True:
#     line = input()
#     if line == 'No Money':
#         break
#     command_args = line.split()
#     command = command_args[0]
#     gift = command_args[1]
#
#     if command == 'OutOfStock':
#         for idx in range(len(gifts)):
#             if gifts[idx] == gift:
#                 gifts[idx] = "None"
#     elif command == "Required":
#         idx = int(command_args[2])
#         if 0 <= idx < len(gifts):
#             gifts[idx] = gift
#     elif command == "JustInCase":
#         gifts[-1] = gift
#
# for gift in gifts:
#     if gift == "None":
#         continue
#     print(gift,end=" ")
# LISTS EX 1.2
# FIRST 1.2
# list_of_numbers = input().split()
# opposite_numbers = []
# for element in list_of_numbers:
#     current_number = -int(element)
#     opposite_numbers.append(current_number)
#
# print(opposite_numbers)
# SECOND 2.2
# factor = int(input())
# count = int(input())
#
# list_of_numbers = []
#
# for multiplier in range(1,count+1):
#     list_of_numbers.append(factor*multiplier)
# print(list_of_numbers)
# THIRD 3.2
# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# ## team_a= ["A-" + str(s) for s in range(1,12)]
# ## team_b= ["B-" + str(s) for s in range(1,12)]
#
# players = input().split()
# game_was_terminated = False
#
# for player in players:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_was_terminated = True
#         break
#
# print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
# if game_was_terminated:
#     print("Game was terminated")
# FOURTH 4.2

# money_list = input().split(", ")
# money_list_as_digit = []
# for element in money_list:
#     money_list_as_digit.append(int(element))
#
# number_of_beggars = int(input())
# final_sums = []
# starting_index = 0
#
# while starting_index < number_of_beggars:
#     sum_for_current_beggar = 0
#
#     for current_index in range(starting_index,len(money_list_as_digit),number_of_beggars):
#         sum_for_current_beggar += money_list_as_digit[current_index]
#
#     final_sums.append(sum_for_current_beggar)
#     starting_index += 1
# print(final_sums)
# TENTH 10.2
# events = input().split("|")
# total_coins = 100
# total_energy = 100
# factory_is_open = True
#
# for event in events:
#     event_items = event.split("-")
#     type_of_event = event_items[0]
#     event_value = int(event_items[1])
#     if type_of_event == "rest":
#         current_energy = total_energy
#         total_energy += event_value
#         if total_energy > 100:
#             total_energy = 100
#         gained_energy = total_energy - current_energy
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {total_energy}.")
#     elif type_of_event == "order":
#         if total_energy >= 30:
#             total_energy -= 30
#             total_coins += event_value
#             print(f"You earned {event_value} coins.")
#         else:
#             total_energy += 50
#             print("You had to rest!")
#     else:
#         if total_coins >= event_value:
#             total_coins -= event_value
#             print(f"You bought {type_of_event}.")
#         else:
#             print(f"Closed! Cannot afford {type_of_event}.")
#             factory_is_open = False
#             break
# if factory_is_open:
#     print("Day completed!")
#     print(f"Coins: {total_coins}")
#     print(f"Energy: {total_energy}")
# FIFTH 5.2

# deck_of_cards = input().split()
# number_of_shuffles = int(input())
#
# for shuffle in range(number_of_shuffles):
#     final_deck = []
#     middle_of_the_deck = len(deck_of_cards)//2
#     left_part = deck_of_cards[0:middle_of_the_deck]
#     right_part = deck_of_cards[middle_of_the_deck:]
#     for card_index in range(len(left_part)):
#         final_deck.append(left_part[card_index])
#         final_deck.append(right_part[card_index])
#     deck_of_cards = final_deck
# print(final_deck)
#
#
# collection_of_items = input().split('|')
# budget = float(input())
# items_to_sell_sum = []
# og_buget = budget
#
# for item in collection_of_items:
#     different_items = item.split("->")
#     type_of_item = different_items[0]
#     price_of_item = float(different_items[1])
#     if price_of_item > budget:
#         continue
#     if type_of_item == 'Clothes':
#         if price_of_item > 50:
#             continue
#         else:
#             budget -= price_of_item
#             items_to_sell_sum.append(price_of_item*1.4)
#     elif type_of_item == 'Shoes':
#         if price_of_item > 35.00:
#             continue
#         else:
#             budget -= price_of_item
#             items_to_sell_sum.append(price_of_item*1.4)
#     elif type_of_item == 'Accessories':
#         if price_of_item > 20.50:
#             continue
#         else:
#             budget -= price_of_item
#             items_to_sell_sum.append(price_of_item*1.4)
#     print(f'{price_of_item*1.4:.2f}',end=" ")
# print()
# profit = sum(items_to_sell_sum) + budget - og_buget
# new_budget = budget + sum(items_to_sell_sum)
#
# print(f"Profit: {profit:.2f}")
# if new_budget >= 150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")


