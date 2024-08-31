from project.army.Army import Army
import project.game_management.enemy_units.enemy_unit_choice_functions as euc


def show_action_choice_screen(armies, screen_type, needed_units):
    screen = screen_type
    for name in needed_units:
        if name in armies[0].get_army_units_names():
            return screen.start_screen_loop()


from project.game_screens.Land_forces_screen import LandForcesScreen
from project.config import LAND_FORCES_NAMES
chosen_units = ["Infantry", "Tanks", "Spies", "Artillery"]
player_army = Army(chosen_units)
enemy_army = Army(euc.iranian_proxy())
armies = [player_army, enemy_army]

show_action_choice_screen(armies, LandForcesScreen(player_army, enemy_army), LAND_FORCES_NAMES)
