from project.Game_screen import GameScreen
from project.general_functions.colors import LIGHT_GREY, LIGHT_BLUE
from project.general_functions.images_functions import get_sprite_paths
from project.Button import Button
import pygame


class Decision_choice_screen(GameScreen):
    def __init__(self):
        super(Decision_choice_screen, self).__init__()
        self.current_game_state = []
        self.button_list = self.get_initial_button_list()
        self.choice = False

    def get_initial_button_list(self):
        button_list = pygame.sprite.Group()
        origin_button_list = self.get_buttons()
        for button in origin_button_list:
            button_list.add(button)
        return button_list

    def get_buttons(self):
        button_list = []
        button_position_list = self.get_button_position_list()
        for i in range(len(button_position_list)):
            string = get_sprite_paths(UNITS_NAMES[i]) # TODO: DECIDE OF BACKEND LOGIC
            button_list.append(Button(button_position_list[i], string, UNITS_NAMES[i])) # TODO: DECIDE OF BACKEND LOGIC
        return button_list

    def get_button_position_list(self):
        return [[0,0]]

    def internal_screen_logic(self, did_user_click):
        if did_user_click:
            self.change_data_according_to_user_actions()
            if self.choice:
                return False
        return True

    def change_data_according_to_user_actions(self):
        return

    def draw_everything(self, screen):
        screen.fill(LIGHT_GREY)
        self.button_list.draw(screen)
        self.draw_unit_choice_text(screen)
        self.draw_mouse(screen)

    def draw_mouse(self, screen):
        pygame.draw.circle(screen, LIGHT_BLUE, (self.mouse_position[0], self.mouse_position[1]), 4)
        pygame.mouse.set_visible(False)

    def draw_unit_choice_text(self, screen):
        return


