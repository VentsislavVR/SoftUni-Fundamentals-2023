def fight_func(line, pool):
    line = line.split(" vs ")
    player1, player2 = line[0], line[1]
    if player1 in pool and player2 in pool:
        for player, skills in pool.items():
            print(f"Player: {player}")
            for skill, value in skills.items():
                print(f"  Skill: {skill}, Value: {value}")
def lets_go():
    hero_pool = {}
    while True:
        line = input()
        if line == "Season end":
            break
        if " -> " in line:
            line = line.split(" -> ")
            player, position, skill = line[0], line[1], int(line[2])
            if player not in hero_pool:
                hero_pool[player] = {position: skill}
            else:
                if player not in hero_pool[player]:
                    hero_pool[player][position] = skill
                elif hero_pool[player][position] < skill:
                    hero_pool[player][position] = skill
        elif "vs" in line:
            fight_func(line, hero_pool)
            # line = line.split("vs")
            # player1 = line[0]
            # player2 = line[1]


lets_go()
