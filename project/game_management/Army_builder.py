from project.army.Army import Army
import project.game_management.enemy_units.enemy_unit_choice_functions as euc
from project.game_screens.Build_army_screen import BuildArmyScreen


class ArmyBuilder:
    def __init__(self):
        self.unit_choice_screen = BuildArmyScreen()

    def build_armies(self):
        chosen_units = self.unit_choice_screen.start_screen_loop()
        player_army = Army(chosen_units)
        enemy_army = Army(euc.iranian_proxy())
        return [player_army, enemy_army]
