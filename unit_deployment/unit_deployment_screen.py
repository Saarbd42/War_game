import unit_deployment.unit_deployment_constants as const
import general_functions.pygame_functions as pyf
import pygame
import unit_deployment.unit_deployment_functions as udf


def show_unit_deployment_screen(player_chosen_units):
    # Constants
    WIDTH, HEIGHT, FPS = const.get_constants()

    # Initialize Pygame
    screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)

    return unit_deployment_game_loop(screen, clock, FPS, player_chosen_units)


def unit_deployment_game_loop(screen, clock, FPS, player_chosen_units):
    running = True
    # Game loop
    while running:
        mouse_position = pyf.get_mouse_position()
        running, did_user_click = user_deployment_events()

        # Game logic

        # Draw everything and update the display
        udf.draw_everything_in_unit_deployment_stage(screen, mouse_position)
        clock = pyf.update_frame(clock, FPS)

    return None


def user_deployment_events():
    # Event handling
    running = True
    did_user_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            did_user_click = True
    return running, did_user_click
