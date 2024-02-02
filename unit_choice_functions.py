import pygame
import button as bt
import images_functions as imf

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (129, 127, 38)


def get_button_list():
    button_list = pygame.sprite.Group()
    origin_button_list = get_unit_buttons()
    for button in origin_button_list:
        button_list.add(button)
    return button_list


def get_unit_buttons():
    infantry_button = bt.Button([50, 100], ["sprites/infantry.png", "sprites/infantry_blue_mark.png"], "infantry")
    tank_button = bt.Button([130, 98], ["sprites/tank.png", "sprites/tank_blue_mark.png"], "tanks")
    atgm_button = bt.Button([250, 100], ["sprites/atgm.png", "sprites/atgm_blue_mark.png"], "tanks")
    plane_button = bt.Button([340, 100], ["sprites/plane.png", "sprites/plane_blue_mark.png"], "tanks")

    return [infantry_button, tank_button, atgm_button, plane_button]


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return [mouse_x, mouse_y]


def button_collision_test(button_list, mouse_position, did_user_click):
    for button in button_list:
        button.check_mouse_collision(mouse_position[0], mouse_position[1], did_user_click)
    return button_list


def how_many_more_units_can_the_player_choose(button_list):
    unit_num = 0
    for button in button_list:
        if button.clicked:
            unit_num += 1
    return unit_num


def draw_everything_in_unit_choice_stage(screen, button_list, mouse_location):
    screen.fill(BROWN)
    button_list.draw(screen)
    draw_unit_choice_text(screen)
    draw_mouse(screen, mouse_location)


def draw_mouse(screen, mouse_location):
    pygame.draw.circle(screen, WHITE, (mouse_location[0], mouse_location[1]), 2)
    pygame.mouse.set_visible(False)


def draw_unit_choice_text(screen):
    draw_the_head_line(screen)
    draw_button_names(screen)


def draw_the_head_line(screen):
    # title_text, title_rect = imf.get_text_stats("You picked " + str(unit_num) + "/4 units", 42, WHITE, [300, 50])
    title_text, title_rect = imf.get_text_stats("Pick 4 units", 42, WHITE, [240, 50])
    imf.draw_titles(screen, [title_text, title_rect])


def draw_button_names(screen):
    unit_names_list = ["Infantry", "Tanks", "Anti-tank", "Air-force"]
    unit_location_list = [[70, 175], [175, 175], [280, 175], [390, 175]]
    for i in range(len(unit_names_list)):
        title_text, title_rect = get_button_title_details(unit_names_list[i], unit_location_list[i])
        imf.draw_titles(screen, [title_text, title_rect])


def get_button_title_details(text, location):
    title_text, title_rect = imf.get_text_stats(text, 30, WHITE, location)
    return title_text, title_rect
