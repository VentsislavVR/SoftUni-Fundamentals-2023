def enroll(hero_pool, hero):
    if hero in hero_pool:
        print(f"{hero} is already enrolled.")
    else:
        hero_pool[hero] = []
    return hero_pool


def learn(hero_pool, hero, spell):
    if hero not in hero_pool:
        print(f"{hero} doesn't exist.")
    else:
        if spell not in hero_pool[hero]:
            hero_pool[hero].append(spell)
        else:
            print(f"{hero} has already learnt {spell}")
    return hero_pool


def unlearn(hero_pool, hero, spell):
    if hero not in hero_pool:
        print(f"{hero} doesn't exist.")
        return hero_pool
    if spell in hero_pool[hero]:
        hero_pool[hero].remove(spell)
    else:
        print(f"{hero} doesn't know {spell}.")
    return hero_pool


def results(heros):
    print("Heroes:")
    for hero, spels in heros.items():
        print(f"== {hero}: {', '.join(spels)}")


hero_pool = {}
while True:
    data = input()
    if data == "End":
        results(hero_pool)
        break

    commands = data.split()

    if commands[0] == "Enroll":
        hero = commands[1]
        hero_pool = enroll(hero_pool, hero)


    elif commands[0] == "Learn":
        hero = commands[1]
        spell = commands[2]
        hero_pool = learn(hero_pool, hero, spell)

    elif commands[0] == "Unlearn":
        hero = commands[1]
        spell = commands[2]
        hero_pool = unlearn(hero_pool, hero, spell)

# o "End"
#
# o "Enroll {HeroName}"
#
# o "Learn {HeroName} {SpellName}"
#
# o "Unlearn {HeroName} {SpellName}


# Enroll Stefan
# Enroll Peter
# Enroll Stefan
# Learn Stefan ItShouldWork
# Learn John ItShouldNotWork
# Unlearn George Dispel
# Unlearn Stefan ItShouldWork
# End

# Enroll Stefan
# Enroll Peter
# Enroll John
# Learn Stefan Spell
# Learn Peter Dispel
# End