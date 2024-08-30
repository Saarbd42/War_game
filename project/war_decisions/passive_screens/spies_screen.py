from project.war_decisions.Decision_choice_screen import DecisionChoiceScreen
import project.general_functions.images_functions as imf
from project.general_functions.colors import BLACK, GREEN, LIGHT_RED, DARK_RED, RED


class SpiesScreen(DecisionChoiceScreen):
    def __init__(self, player_army, enemy_army):
        super(SpiesScreen, self).__init__(player_army, enemy_army)

    @staticmethod
    def get_button_position_list():
        return [[100, 100], [300, 100], [100, 220], [300, 220]]

    def get_relevant_units(self):
        enemy_army = self.current_game_state[1]
        return enemy_army.get_army_units_names()

    def change_data_according_to_user_actions(self):
        self.choice = True

    def draw_unit_choice_text(self, screen):
        self.draw_the_head_line(screen)
        self.draw_button_names(screen)
        return

    @staticmethod
    def draw_the_head_line(screen):
        title_text, title_rect = imf.get_text_stats("The Enemy Army", 60, RED, [240, 40])
        imf.draw_titles(screen, [title_text, title_rect])

    def draw_button_names(self, screen):
        unit_location_list = self.get_button_position_list()
        for i in range(len(unit_location_list)):
            unit_location_list[i][1] += 85
            unit_location_list[i][0] += 40
            title_text, title_rect = imf.get_text_stats(f"Life: {self.current_game_state[1].units[i].life}", 32, GREEN,
                                                        unit_location_list[i])
            imf.draw_titles(screen, [title_text, title_rect])