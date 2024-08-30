from project.base_classes.Decision_choice_screen import DecisionChoiceScreen
from project.general_functions.colors import BLACK, GREEN, LIGHT_BLUE
import project.general_functions.images_functions as imf


class BuildArmyScreen(DecisionChoiceScreen):
    def __init__(self):
        super(BuildArmyScreen, self).__init__([], [])
        self.units_num = 0
        self.all_units_names = ["Infantry", "Tanks", "Artillery", "Air-force",
                                "Missiles", "Air-defence", "Spies", "Cyber"]

    @staticmethod
    def get_button_position_list():
        button_positions = [[50, 100], [130, 98], [250, 100], [352, 90],
                            [50, 220], [165, 220], [278, 220], [355, 220]]
        return button_positions

    def get_relevant_units(self):
        return self.all_units_names

    def change_data_according_to_user_actions(self, did_user_click):
        self.button_collision_test(did_user_click)
        self.units_num = self.how_many_units_the_player_choose()
        self.current_game_state = self.which_units_did_player_choose()
        if self.units_num == 4:
            self.end = True

    def draw_unit_choice_text(self, screen):
        # Write according a specific screen
        self.draw_the_head_line(screen)
        chosen_unit_list = self.which_units_did_player_choose()
        self.draw_button_names(screen, chosen_unit_list)

    '''
    DRAWING FUNCTIONS FOR THE TEXT IN THIS SCREEN
    '''
    def draw_the_head_line(self, screen):
        title_text, title_rect = imf.get_text_stats("Pick " + str(4 - self.units_num) + " units", 60, BLACK, [240, 40])
        imf.draw_titles(screen, [title_text, title_rect])

    def draw_button_names(self, screen, chosen_unit_list):
        button_location_list = [[70, 175], [175, 175], [280, 175], [390, 175],
                              [70, 300], [190, 300], [300, 300], [390, 300]]

        for i in range(len(button_location_list)):
            title_text, title_rect = self.get_button_title_details(self.all_units_names[i], button_location_list[i], chosen_unit_list)
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

    '''
    HELP FUNCTIONS FOR THIS SCREEN
    '''
    def button_collision_test(self, did_user_click):
        for button in self.button_list:
            button.check_mouse_collision(self.mouse_position[0], self.mouse_position[1], did_user_click)

    def how_many_units_the_player_choose(self):
        unit_num = 0
        for button in self.button_list:
            if button.clicked:
                unit_num += 1
        return unit_num

    def which_units_did_player_choose(self):
        unit_list = []
        for button in self.button_list:
            if button.clicked:
                unit_list.append(str(button.unit))
        return unit_list
