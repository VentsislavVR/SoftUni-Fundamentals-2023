needed_exp = float(input())
total_battles = int(input())

exp_gained = 0
battle_counter = 0
has_exp = False
for bat in range(1,total_battles+1):

    if exp_gained >= needed_exp:
        has_exp = True
        break
    current_exp = float(input())
    if bat % 3 == 0:
        current_exp *= 1.15
    elif bat % 5 == 0:
        current_exp *= 0.90
    elif bat % 15 ==0:
        current_exp *= 1.05
    battle_counter += 1
    exp_gained += current_exp

if exp_gained >= needed_exp:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_exp-exp_gained:.2f} more needed.")




