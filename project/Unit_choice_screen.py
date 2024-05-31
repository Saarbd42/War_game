import project.Game_screen as gs
import pygame


class Unit_choice_screen(gs.Game_screen):
    def __init__(self):
        super(Unit_choice_screen, self).__init__()

    def screen_logic(self, current_game_state):
        return current_game_state

    def unit_choice_logic(self, current_game_state):
        units_num, chosen_units = \
            current_game_state[0], current_game_state[1]

    #     # return

    # def get_button_list(self):
    #     button_list = pygame.sprite.Group()
    #     origin_button_list = get_unit_buttons()
    #     for button in origin_button_list:
    #         button_list.add(button)
    #     return button_list

    # def get_unit_buttons(self):
    #     button_list = []
    #     button_position_list = [[50, 100], [130, 98], [250, 100], [352, 90],
    #                             [50, 220], [165, 220], [278, 220], [355, 220]]
    #     for i in range(len(button_position_list)):
    #         string = get_sprite_paths(UNITS_NAMES[i])
    #         button_list.append(bt.Button(button_position_list[i], string, UNITS_NAMES[i]))
    #     return button_list
