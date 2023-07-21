def cast_spell_func(hero_name, needed_magic_power, spell_name, data):
    # the hero casts a spell reducing the mp
    if data[hero_name][1] >= needed_magic_power:
        data[hero_name][1] -= needed_magic_power
        print(f"{hero_name} has successfully cast {spell_name} and now has {data[hero_name][1]} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage_func(hero_name, damage, attacker, data):
    # our hero takes damage,the function prints the death of the hero or dmg taken
    data[hero_name][0] -= damage
    if data[hero_name][0] <= 0:
        print(f"{hero_name} has been killed by {attacker}!")
        data.pop(hero_name)
    else:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {data[hero_name][0]} HP left!")


def recharge_func(hero, amount, data):
    # the hero replenishes his MP
    max_mp = 200
    currenr_mp = data[hero][1]
    if data[hero][1] + amount> max_mp:
        recovered = max_mp - currenr_mp
        data[hero][1] = max_mp
    else:
        data[hero][1] += amount
        recovered = amount
    print(f"{hero} recharged for {recovered} MP!")


def healing_func(hero, amount, data):
    # the hero heals for a certain amount
    max_hp = 100
    currenr_hp = data[hero][0]

    if data[hero][0]+amount > max_hp:
        recovered = max_hp - currenr_hp
        data[hero][0] = max_hp
    else:
        data[hero][0] += amount
        recovered = amount
    print(f"{hero} healed for {abs(recovered)} HP!")


def grande_finally_func(data):
    # this function prints the desired result
    for key,value in data.items():
        hp = value[0]
        mp = value[1]
        print(f"{key}\n  HP: {hp}\n  MP: {mp}")


def store_hero_func(number):
    # this is the initial func in which we get our hero "pool"
    hero_pool = {}
    for _ in range(number):
        current_data = input().split()
        hero = current_data[0]
        health_points = int(current_data[1])
        magic_power = int(current_data[2])
        if health_points > 100:
            health_points = 100
        if magic_power > 200:
            magic_power = 200
        hero_pool[hero] = [health_points, magic_power]
    return hero_pool


def heroes_func(number):
    # this is the main "game" function
    data = store_hero_func(number)

    while True:

        command = input().split(" - ")
        if command[0] == "End":
            grande_finally_func(data)
            break
        orders = command[0]
        hero_name = command[1]
        if orders == "CastSpell":
            needed_magic_power = int(command[2])
            spell_name = command[3]
            cast_spell_func(hero_name, needed_magic_power, spell_name, data)

        elif orders == "TakeDamage":
            damage = int(command[2])
            attacker = command[3]
            take_damage_func(hero_name, damage, attacker, data)

        elif orders == "Recharge":
            amount = int(command[2])
            recharge_func(hero_name, amount, data)

        elif orders == "Heal":
            amount = int(command[2])
            healing_func(hero_name, amount, data)


number_of_heroes = int(input())
heroes_func(number_of_heroes)
