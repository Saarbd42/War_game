import unit_choice.unit_choice_screen as ucs
import unit_deployment.unit_deployment_screen as uds
import enemy_unit_choice.enemy_choice_screen as ecs
import enemy_unit_choice.enemy_unit_choice_functions as ecf
import army.army_functions as army_f


def get_game_armies():
    enemy_chosen_units, enemy_army_data = ecf.randomly_choose_enemy_units()
    player_army_data = player_choose_and_deploy_army(enemy_chosen_units)
    return army_f.build_armies(player_army_data, enemy_army_data)


def player_choose_and_deploy_army(enemy_chosen_units):
    player_chosen_units = ucs.show_unit_choice_screen()
    ecs.show_enemy_choice_screen(player_chosen_units, enemy_chosen_units)
    player_unit_deployment, player_non_deployable_units = uds.show_unit_deployment_screen(player_chosen_units)
    return [player_unit_deployment, player_non_deployable_units]
