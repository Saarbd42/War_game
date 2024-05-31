import pygame
import sys
import project.enemy_unit_choice.enemy_unit_choice_functions as ecf
import project.main_game_functions as mgf
import project.army.army_functions as army_f
import project.strategy_choice.strategy_choice_screen as scs

player_army, enemy_army = mgf.get_game_armies()

# Game_Loop
player_army, enemy_army = army_f.update_which_units_are_exposed(player_army, enemy_army)
scs.show_strategy_screen(player_army, enemy_army)

# FOR TESTING ONLY
###################################
for unit in player_army.unit_list:
    print(unit.type)
    print(unit.exposed)
for unit in enemy_army.unit_list:
    print(unit.type)
    print(unit.exposed)
####################################

pygame.quit()
sys.exit()
