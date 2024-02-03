import unit_deployment.unit_deployment_constants as const
import general_functions.pygame_functions as pyf
import pygame
import unit_deployment.unit_deployment_functions as udf
import unit_deployment.unit_deployment_buttons_functions as dbf


def show_unit_deployment_screen(player_chosen_units):
    # Constants
    WIDTH, HEIGHT, FPS = const.get_constants()

    # Initialize Pygame
    screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)

    return unit_deployment_game_loop(screen, clock, FPS, player_chosen_units)


def unit_deployment_game_loop(screen, clock, FPS, player_chosen_units):
    running, deployment, player_chosen_units, current_button = \
        get_initial_unit_deployment_variables(player_chosen_units)

    # Game loop
    while running:
        mouse_position = pyf.get_mouse_position()
        running, did_user_click = user_deployment_events()

        # Game logic
        current_button.check_mouse_collision(mouse_position[0], mouse_position[1], did_user_click)
        if ready_to_deploy(current_button, did_user_click, mouse_position):
            new_deployment = deploy_troop_to_territory(mouse_position, current_button)
            new_deployment = check_if_crowded_in_territory(deployment, new_deployment)
            deployment.append(new_deployment)
            player_chosen_units, current_button = dbf.get_next_button(player_chosen_units)

        # Draw everything and update the display
        udf.draw_everything_in_unit_deployment_stage(screen, mouse_position, current_button, deployment)
        clock = pyf.update_frame(clock, FPS)
    return deployment


def get_initial_unit_deployment_variables(player_chosen_units):
    running = True
    deployment = []
    player_chosen_units, current_button = dbf.get_next_button(player_chosen_units)
    # JUST FOR TEST
    player_chosen_units.append("Tanks")
    # JUST FOR TEST
    return running, deployment, player_chosen_units, current_button


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


def check_if_crowded_in_territory(deployment_list, new_deployment):
    if len(deployment_list) > 0:
        for deployment in deployment_list:
            if deployment[0] == new_deployment[0]:
                new_deployment[2] += 1
    return new_deployment


def deploy_troop_to_territory(mouse_position, current_button):
    if mouse_position[0] < 120:
        return [1, current_button.unit, 0]
    elif mouse_position[0] < 240:
        return [2, current_button.unit, 0]
    else:
        return [3, current_button.unit, 0]


def ready_to_deploy(current_button, did_user_click, mouse_position):
    if current_button.clicked and did_user_click and is_mouse_on_deployment_territory(mouse_position):
        return True
    return False


def is_mouse_on_deployment_territory(mouse_position):
    if mouse_position[1] > 180 and mouse_position[0] < 360:
        return True
    else:
        return False
