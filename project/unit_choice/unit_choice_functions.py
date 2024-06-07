import pygame
import project.Button as bt
import project.general_functions.images_functions as imf
from project.general_functions.colors import BLACK, LIGHT_BLUE, LIGHT_GREY

UNITS_NAMES = ["Infantry", "Tanks", "Artillery", "Air-force",
               "Missiles", "Air-defence", "Spies", "Cyber"]


def get_button_list():
    button_list = pygame.sprite.Group()
    origin_button_list = get_unit_buttons()
    for button in origin_button_list:
        button_list.add(button)
    return button_list


def get_unit_buttons():
    button_list = []
    button_position_list = [[50, 100], [130, 98], [250, 100], [352, 90],
                            [50, 220], [165, 220], [278, 220], [355, 220]]
    for i in range(len(button_position_list)):
        string = get_sprite_paths(UNITS_NAMES[i])
        button_list.append(bt.Button(button_position_list[i], string, UNITS_NAMES[i]))
    return button_list


def get_sprite_paths(sprite_name):
    initial_path = r'C:\Users\97252\Desktop\CS\PersonalProjects\War_game\sprites\\'
    string = [initial_path + str(sprite_name) + ".png",
              initial_path + str(sprite_name) + "_blue_mark.png"]
    return string


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return [mouse_x, mouse_y]


def button_collision_test(button_list, mouse_position, did_user_click):
    for button in button_list:
        button.check_mouse_collision(mouse_position[0], mouse_position[1], did_user_click)
    return button_list


def which_units_did_player_choose(button_list):
    unit_list = []
    for button in button_list:
        if button.clicked:
            unit_list.append(str(button.unit))
    return unit_list


def how_many_more_units_can_the_player_choose(button_list):
    unit_num = 0
    for button in button_list:
        if button.clicked:
            unit_num += 1
    return unit_num


def draw_everything_in_unit_choice_stage(screen, button_list, mouse_location, units_num):
    screen.fill(LIGHT_GREY)
    button_list.draw(screen)
    draw_unit_choice_text(screen, button_list, units_num)
    draw_mouse(screen, mouse_location)


def draw_mouse(screen, mouse_location):
    pygame.draw.circle(screen, LIGHT_BLUE, (mouse_location[0], mouse_location[1]), 4)
    pygame.mouse.set_visible(False)


def draw_unit_choice_text(screen, button_list, units_num):
    draw_the_head_line(screen, units_num)
    chosen_unit_list = which_units_did_player_choose(button_list)
    draw_button_names(screen, chosen_unit_list)


def draw_the_head_line(screen, units_num):
    title_text, title_rect = imf.get_text_stats("Pick " + str(4 - units_num) + " units", 60, BLACK, [240, 40])
    imf.draw_titles(screen, [title_text, title_rect])


def draw_button_names(screen, chosen_unit_list):
    unit_location_list = [[70, 175], [175, 175], [280, 175], [390, 175],
                          [70, 300], [190, 300], [300, 300], [390, 300]]
    for i in range(len(UNITS_NAMES)):
        title_text, title_rect = get_button_title_details(UNITS_NAMES[i], unit_location_list[i], chosen_unit_list)
        imf.draw_titles(screen, [title_text, title_rect])


def get_button_title_details(unit_name, unit_location, chosen_unit_list):
    if unit_name in chosen_unit_list:
        title_text, title_rect = get_chosen_button_title_details(unit_name, unit_location)
    else:
        title_text, title_rect = get_normal_button_title_details(unit_name, unit_location)
    return title_text, title_rect


def get_chosen_button_title_details(text, location):
    title_text, title_rect = imf.get_text_stats(text, 30, LIGHT_BLUE, location)
    return title_text, title_rect


def get_normal_button_title_details(text, location):
    title_text, title_rect = imf.get_text_stats(text, 30, BLACK, location)
    return title_text, title_rect
