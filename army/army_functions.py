from army.Army import Army


def update_which_units_are_exposed(player_army, enemy_army):
    player_army.check_which_units_are_exposed(enemy_army)
    enemy_army.check_which_units_are_exposed(player_army)
    return player_army, enemy_army


def build_armies(player_army_data, enemy_army_data):
    player_army = Army(player_army_data[0], player_army_data[1], False)
    enemy_army = Army(enemy_army_data[0], enemy_army_data[1], True)
    return player_army, enemy_army
