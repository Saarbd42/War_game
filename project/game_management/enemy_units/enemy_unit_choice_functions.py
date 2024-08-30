import random


def get_iranian_proxy():
    return iranian_proxy()


def randomly_choose_enemy_units():
    random_num = random.randint(1, 4)
    if random_num == 1:
        return israel_6_day_war()
    elif random_num == 2:
        return egypt_1973_war()
    elif random_num == 3:
        return iranian_proxy()
    else:
        return modern_russia()


def israel_6_day_war():
    chosen_units = ["Infantry", "Tanks", "Air-force", "Spies"]
    return chosen_units


def egypt_1973_war():
    chosen_units = ["Infantry", "Tanks", "Anti-tank", "Air-defence"]
    return chosen_units


def iranian_proxy():
    chosen_units = ["Infantry", "Artillery", "Missiles", "Air-defence"]
    return chosen_units


def modern_russia():
    chosen_units = ["Tanks", "Cyber", "Missiles", "Air-force"]
    return chosen_units
