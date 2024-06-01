import project.Game_screen as gs
from project.unit_choice import unit_choice_functions as ucf
from project.general_functions.colors import LIGHT_GREY
import pygame


class Unit_choice_screen(gs.Game_screen):
    def __init__(self):
        super(Unit_choice_screen, self).__init__()
        self.current_game_state = []
        self.button_list = None
        self.units_num = 0

    def screen_logic(self):
        running, did_user_click = self.user_choice_events()
        self.mouse_position = self.get_mouse_position()
        return self.unit_choice_logic(did_user_click)

    def unit_choice_logic(self, did_user_click):
        self.update_button_list(did_user_click)
        if did_user_click:
            self.change_data_according_to_user_actions()
            if self.units_num == 4:
                return False
        return True

    def update_button_list(self, did_user_click):
        if self.button_list is None:
            self.button_list = ucf.get_button_list()
        else:
            self.button_list = ucf.button_collision_test(self.button_list, self.mouse_position, did_user_click)

    def change_data_according_to_user_actions(self):
        self.units_num = ucf.how_many_more_units_can_the_player_choose(self.button_list)
        self.current_game_state = ucf.which_units_did_player_choose(self.button_list)

    def draw_everything(self, screen):
        self.draw_everything_in_unit_choice_stage(screen)

    def draw_everything_in_unit_choice_stage(self, screen):
        screen.fill(LIGHT_GREY)
        self.button_list.draw(screen)
        ucf.draw_unit_choice_text(screen, self.button_list, self.units_num)
        ucf.draw_mouse(screen, self.mouse_position)
