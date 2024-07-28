from project.army.Army import Army
import project.unit_choice.enemy_unit_choice.enemy_unit_choice_functions as euc
from project.unit_choice.Unit_choice_screen import Unit_choice_screen


class ArmyBuilder:
    def __init__(self):
        self.unit_choice_screen = Unit_choice_screen()

    def build_armies(self):
        chosen_units = self.unit_choice_screen.start_screen_loop()
        player_army = Army(chosen_units)
        enemy_army = Army(euc.iranian_proxy())
        return [player_army, enemy_army]
