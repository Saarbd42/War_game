import random


def randomly_choose_enemy_units():
    random_num = random.randint(1, 4)
    if random_num == 1:
        enemy_units_list = israel_6_day_war()
    elif random_num == 2:
        enemy_units_list = egypt_1973_war()
    elif random_num == 3:
        enemy_units_list = iranian_proxy()
    else:
        enemy_units_list = modern_russia()
    return enemy_units_list


def israel_6_day_war():
    return ["Infantry", "Tanks", "Air-force", "Spies"]


def egypt_1973_war():
    return ["Infantry", "Tanks", "Anti-tank", "Air-defence"]


def iranian_proxy():
    return ["Infantry", "Anti-tank", "Missiles", "Air-defence"]


def modern_russia():
    return ["Tanks", "Cyber", "Missiles", "Air-force"]
