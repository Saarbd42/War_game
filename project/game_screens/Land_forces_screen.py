from project.base_classes.Decision_choice_screen import DecisionChoiceScreen
from project.general_functions.colors import BLACK, LIGHT_BLUE
import project.general_functions.images_functions as imf
from project.config import LAND_FORCES_NAMES


class LandForcesScreen(DecisionChoiceScreen):
    def __init__(self, player_army, enemy_army):
        super(LandForcesScreen, self).__init__(player_army, enemy_army)
        self.total_button_num = len(self.get_relevant_units())

    def get_button_position_list(self):
        return [[100, 100], [300, 100], [100, 220], [300, 220], [300, 300]][:self.total_button_num]

    def get_relevant_units(self):
        player_army = self.current_game_state[0]
        additional = ["Sword", "Shield"]
        land_forces = []
        for name in player_army.get_army_units_names():
            if name in LAND_FORCES_NAMES:
                land_forces.append(name)
        return land_forces + additional

    def change_data_according_to_user_actions(self, did_user_click):
        return

    def draw_unit_choice_text(self, screen):
        # Write according a specific screen
        return
