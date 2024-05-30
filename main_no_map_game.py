import project.unit_choice.unit_choice_screen as ucs
import project.enemy_unit_choice.enemy_choice_screen as ecs
import project.enemy_unit_choice.enemy_unit_choice_functions as ecf

player_chosen_units = ucs.show_unit_choice_screen()
enemy_chosen_units, enemy_army_data = ecf.get_iranian_proxy()
print(enemy_chosen_units)
print(player_chosen_units)