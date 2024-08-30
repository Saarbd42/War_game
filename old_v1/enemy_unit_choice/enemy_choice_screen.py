import project.unit_choice.unit_choice_constants as const
import project.general_functions.images_functions as imf
import project.general_functions.pygame_functions as pyf
import project.enemy_unit_choice.enemy_unit_choice_functions as eucf
import pygame
import project.general_functions.colors as cl

BROWN = (129, 127, 38)
BLACK = (0, 0, 0)
LIGHT_GREY = (237, 237, 242)


def show_enemy_choice_screen(player_units, enemy_chosen_units):
    if check_for_spies(player_units):
        # Constants
        WIDTH, HEIGHT, FPS = const.get_constants()
        # Initialize Pygame
        screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)
        enemy_choice_game_loop(screen, clock, FPS, enemy_chosen_units)


def enemy_choice_game_loop(screen, clock, FPS, enemy_chosen_units):
    running = True
    # Game loop
    while running:

        mouse_position = pyf.get_mouse_position()
        running, did_user_click = pyf.user_events()

        # Game logic
        position_list, path_list = get_enemy_details(enemy_chosen_units)
        if did_user_click:
            running = False

        # Draw everything and update the display
        draw_everything_in_enemy_choice_stage(screen, position_list, path_list, mouse_position)
        clock = pyf.update_frame(clock, FPS)


def check_for_spies(player_units):
    if "Spies" in player_units:
        return True
    return False


def draw_everything_in_enemy_choice_stage(screen, position_list, path_list, mouse_position):
    screen.fill(LIGHT_GREY)
    draw_enemy_units(screen, position_list, path_list)
    draw_enemy_choice_text(screen)
    pyf.draw_mouse(screen, mouse_position)


def draw_enemy_choice_text(screen):
    draw_enemy_choice_head_line(screen)
    draw_enemy_choice_bottom_line(screen)


def draw_enemy_choice_head_line(screen):
    title_text, title_rect = imf.get_text_stats("The enemy picked:", 60, cl.DARK_RED, [240, 50])
    imf.draw_titles(screen, [title_text, title_rect])


def draw_enemy_choice_bottom_line(screen):
    title_text, title_rect = imf.get_text_stats("Click anywhere to continue", 45, cl.DARK_RED, [240, 330])
    imf.draw_titles(screen, [title_text, title_rect])


def draw_enemy_units(screen, position_list, path_list):
    for i in range(len(path_list)):
        enemy_unit_image, enemy_unit_rect = get_enemy_unit_details(path_list[i], position_list[i])
        screen.blit(enemy_unit_image, enemy_unit_rect)
        title_text, title_rect = get_enemy_unit_text_details(path_list[i], position_list[i])
        imf.draw_titles(screen, [title_text, title_rect])


def get_enemy_unit_text_details(path, position):
    enemy_unit_name = get_name_from_path(path)
    title_text, title_rect = imf.get_text_stats(enemy_unit_name, 30, cl.DARK_RED,
                                                [position[0], position[1] + 80])
    return title_text, title_rect


def get_name_from_path(path):
    name = path.split("/")[1]
    name = name.split("_")[0]
    return name


def get_enemy_unit_details(enemy_unit_path, enemy_unit_position):
    enemy_unit_image = get_enemy_unit_image(enemy_unit_path)
    enemy_unit_rect = get_enemy_unit_rect(enemy_unit_image, enemy_unit_position)
    return enemy_unit_image, enemy_unit_rect


def get_enemy_unit_image(enemy_unit_path):
    unit_image = pygame.image.load(enemy_unit_path)
    unit_image.set_colorkey((163, 73, 164))
    return unit_image


def get_enemy_unit_rect(enemy_unit_image, enemy_unit_position):
    unit_rect = enemy_unit_image.get_rect()
    unit_rect.x = enemy_unit_position[0] - unit_rect.width / 2
    unit_rect.y = enemy_unit_position[1]
    return unit_rect


def get_enemy_details(enemy_unit_list):
    position_list = [[150, 100], [300, 100], [150, 200], [300, 200]]
    path_list = []
    for enemy_unit_name in enemy_unit_list:
        string = get_enemy_sprite_path(enemy_unit_name)
        path_list.append(string)
    return position_list, path_list


def get_enemy_sprite_path(enemy_unit_name):
    string = "sprites/" + str(enemy_unit_name) + "_red_mark.png"
    return string
