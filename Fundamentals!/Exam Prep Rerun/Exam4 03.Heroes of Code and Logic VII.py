MAX_HP = 100
MAX_MANA = 200


def cast_spell(heroes, hero, mp, spell):
    if heroes[hero]["mana"] >= mp:
        heroes[hero]["mana"] -= mp
        print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['mana']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")


def take_dmg(heroes, hero, damage, attacker):
    heroes[hero]["health"] -= damage
    if heroes[hero]["health"] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['health']} HP left!")
    else:
        del heroes[hero]
        print(f"{hero} has been killed by {attacker}!")


def recharge(heroes, hero, mp):
    current_mana = heroes[hero]["mana"]
    heroes[hero]["mana"] += mp
    if heroes[hero]["mana"] > MAX_MANA:
        heroes[hero]["mana"] = MAX_MANA
        recharget_amount = MAX_MANA - current_mana
        print(f"{hero} recharged for {recharget_amount} MP!")
    else:
        print(f"{hero} recharged for {mp} MP!")


def heal(heroes, hero, hp):
    current_health = heroes[hero]["health"]
    heroes[hero]["health"] += hp
    if heroes[hero]["health"] > MAX_HP:
        heroes[hero]["health"] = MAX_HP
        healed_amount = MAX_HP - current_health
        print(f"{hero} healed for {healed_amount} HP!")
    else:
        print(f"{hero} healed for {hp} HP!")


def get_heroes(hero_count):
    heroes = {}
    for h in range(hero_count):
        hero, health, mana = input().split()
        heroes[hero] = {"health": int(health), "mana": int(mana)}
    return heroes


def results(heroes):
    for hero, stats in heroes.items():
        print(f"{hero} \n HP: {stats['health']} \n MP: {stats['mana']}")


def game(heroes):
    heroes = get_heroes(hero_count)
    while True:
        command = input()
        if command == "End":
            results(heroes)
            break

        data = command.split(" - ")
        action = data[0]
        hero = data[1]

        if action == "CastSpell":
            mp_needed = int(data[2])
            spell_name = data[3]
            cast_spell(heroes, hero, mp_needed, spell_name)
        elif action == "TakeDamage":
            damage = int(data[2])
            attacker = data[3]
            take_dmg(heroes, hero, damage, attacker)
        elif action == "Recharge":
            mp = int(data[2])
            recharge(heroes, hero, mp)
        elif action == "Heal":
            hp = int(data[2])
            heal(heroes, hero, hp)


hero_count = int(input())
game(get_heroes)
