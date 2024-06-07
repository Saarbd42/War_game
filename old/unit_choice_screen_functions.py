import pygame
import project.unit_choice.unit_choice_constants as const
import project.general_functions.pygame_functions as pyf
import project.unit_choice.unit_choice_functions as ucf


def show_unit_choice_screen():
    # Constants
    WIDTH, HEIGHT, FPS = const.get_constants()

    # Initialize Pygame
    screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)

    return unit_choice_game_loop(screen, clock, FPS)


def unit_choice_game_loop(screen, clock, FPS):

    button_list, units_num, chosen_units, running = get_all_initial_game_loop_variables()

    # Game loop
    while running:

        mouse_position = ucf.get_mouse_position()
        running, did_user_click = user_choice_events()

        # Game logic
        button_list = ucf.button_collision_test(button_list, mouse_position, did_user_click)
        if did_user_click:
            units_num, chosen_units = change_user_choices(button_list)
            if units_num == 4:
                running = False

        # Draw everything and update the display
        ucf.draw_everything_in_unit_choice_stage(screen, button_list, mouse_position, units_num)
        clock = pyf.update_frame(clock, FPS)

    return chosen_units


def change_user_choices(button_list):
    units_num = ucf.how_many_more_units_can_the_player_choose(button_list)
    chosen_units = ucf.which_units_did_player_choose(button_list)
    return units_num, chosen_units


def user_choice_events():
    # Event handling
    running = True
    did_user_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            did_user_click = True
    return running, did_user_click


def get_all_initial_game_loop_variables():
    # Define buttons
    button_list = ucf.get_button_list()
    units_num = 0
    chosen_units = []
    running = True

    return button_list, units_num, chosen_units, running
