import random


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
    deployed_units = [[4, 'Infantry', 0], [4, 'Tanks', 1], [6, "Air-force", 0]]
    non_deployed_units = ["Spies"]
    return chosen_units, [deployed_units, non_deployed_units]


def egypt_1973_war():
    chosen_units = ["Infantry", "Tanks", "Anti-tank", "Air-defence"]
    deployed_units = [[4, 'Infantry', 0], [4, 'Tanks', 1], [4, "Anti-tank", 2], [4, "Air-defence", 3]]
    non_deployed_units = []
    return chosen_units, [deployed_units, non_deployed_units]


def iranian_proxy():
    chosen_units = ["Infantry", "Anti-tank", "Missiles", "Spies"]
    deployed_units = [[6, 'Infantry', 0], [6, 'Anti-tank', 1], [6, "Missiles", 2]]
    non_deployed_units = ["Spies"]
    return chosen_units, [deployed_units, non_deployed_units]


def modern_russia():
    chosen_units = ["Tanks", "Cyber", "Missiles", "Air-force"]
    deployed_units = [[4, 'Tanks', 0], [6, "Missiles", 0], [6, "Air-force", 1]]
    non_deployed_units = ["Cyber"]
    return chosen_units, [deployed_units, non_deployed_units]
