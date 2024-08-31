from project.base_classes.Decision_choice_screen import DecisionChoiceScreen
from project.general_functions.colors import BLACK, LIGHT_BLUE
import project.general_functions.images_functions as imf
from project.config import LAND_FORCES_NAMES


class LandForcesScreen(DecisionChoiceScreen):
    def __init__(self, player_army, enemy_army):
        super(LandForcesScreen, self).__init__(player_army, enemy_army)
        self.total_button_num = len(self.get_relevant_units())

    def get_button_position_list(self):
        units_positions = [[30, 80], [30, 180], [30, 280]][:self.total_button_num - 2]
        attack_def_positions = [[220, 70], [220, 250]]
        return units_positions + attack_def_positions

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
        self.draw_the_head_line(screen)
        # chosen_unit_list = self.which_units_did_player_choose()
        # self.draw_button_names(screen, chosen_unit_list)

    '''
    DRAWING FUNCTIONS FOR THE TEXT IN THIS SCREEN
    '''

    def draw_the_head_line(self, screen):
        title_text, title_rect = imf.get_text_stats("WHAT SHOULD OUR LAND FORCES DO?", 34, BLACK, [240, 30])
        imf.draw_titles(screen, [title_text, title_rect])

    def draw_button_names(self, screen, chosen_unit_list):
        button_location_list = [[70, 175], [175, 175], [280, 175], [390, 175],
                                [70, 300], [190, 300], [300, 300], [390, 300]]

        for i in range(len(button_location_list)):
            title_text, title_rect = self.get_button_title_details(self.all_units_names[i], button_location_list[i],
                                                                   chosen_unit_list)
            imf.draw_titles(screen, [title_text, title_rect])

    def get_button_title_details(self, unit_name, unit_location, chosen_unit_list):
        if unit_name in chosen_unit_list:
            title_text, title_rect = self.get_chosen_button_title_details(unit_name, unit_location)
        else:
            title_text, title_rect = self.get_normal_button_title_details(unit_name, unit_location)
        return title_text, title_rect

    @staticmethod
    def get_chosen_button_title_details(text, location):
        title_text, title_rect = imf.get_text_stats(text, 30, LIGHT_BLUE, location)
        return title_text, title_rect

    @staticmethod
    def get_normal_button_title_details(text, location):
        title_text, title_rect = imf.get_text_stats(text, 30, BLACK, location)
        return title_text, title_rect

