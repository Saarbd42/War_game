import unit_deployment.unit_deployment_constants as const
import general_functions.pygame_functions as pyf
import pygame
import unit_deployment.unit_deployment_drawing_functions as udf
import unit_deployment.unit_deployment_buttons_functions as dbf


def show_unit_deployment_screen(player_chosen_units):
    # Constants
    WIDTH, HEIGHT, FPS = const.get_constants()

    # Initialize Pygame
    screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)

    player_chosen_units, spies_and_cyber = remove_non_deployable(player_chosen_units)
    return unit_deployment_game_loop(screen, clock, FPS, player_chosen_units), spies_and_cyber


def remove_non_deployable(player_chosen_units):
    new_player_chosen_units, spies_and_cyber = [], []
    for unit in player_chosen_units:
        if is_deployable_unit(unit):
            new_player_chosen_units.append(unit)
        else:
            spies_and_cyber.append(unit)
    return new_player_chosen_units, spies_and_cyber


def is_deployable_unit(unit):
    if unit != "Cyber" and unit != "Spies":
        return True
    return False


def unit_deployment_game_loop(screen, clock, FPS, player_chosen_units):
    running, deployment, player_chosen_units, current_button = \
        get_initial_unit_deployment_variables(player_chosen_units)

    while running:
        mouse_position, did_user_click, running = get_user_input()

        # Game logic
        current_button.check_mouse_collision(mouse_position[0], mouse_position[1], did_user_click)
        if ready_to_deploy(current_button, did_user_click, mouse_position):
            if not check_if_territory_crowded(mouse_position, current_button, deployment):
                deployment = add_new_deployment(deployment, mouse_position, current_button)
                player_chosen_units, current_button, running = update_stats_for_next_deployment(player_chosen_units,
                                                                                            current_button)
            if not running:
                return deployment

        # Draw everything and update the display
        udf.draw_everything_in_unit_deployment_stage(screen, mouse_position, current_button, deployment)
        clock = pyf.update_frame(clock, FPS)


def update_stats_for_next_deployment(player_chosen_units, current_button):
    if player_finished_deployment(player_chosen_units):
        return player_chosen_units, current_button, False
    else:
        player_chosen_units, current_button = dbf.get_next_button(player_chosen_units)
        return player_chosen_units, current_button, True


def get_user_input():
    mouse_position = pyf.get_mouse_position()
    running, did_user_click = user_deployment_events()
    return mouse_position, did_user_click, running


def add_new_deployment(deployment, mouse_position, current_button):
    new_deployment = deploy_troop(mouse_position, current_button, deployment)
    deployment.append(new_deployment)
    return deployment


def player_finished_deployment(player_chosen_units):
    if len(player_chosen_units) == 0:
        return True
    return False


def get_initial_unit_deployment_variables(player_chosen_units):
    running = True
    deployment = []
    player_chosen_units, current_button = dbf.get_next_button(player_chosen_units)
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


def deploy_troop(mouse_position, current_button, deployment):
    new_deployment = deploy_troop_to_territory(mouse_position, current_button)
    # can_player_put_there = check_if_crowded_in_territory(deployment, new_deployment)
    return new_deployment


def deploy_troop_to_territory(mouse_position, current_button):
    x_position = int(mouse_position[0] / 120) + 1
    y_position = int((mouse_position[1] - 180) / 60)
    return [x_position, current_button.unit, y_position]


def ready_to_deploy(current_button, did_user_click, mouse_position):
    if current_button.clicked and did_user_click and is_mouse_on_deployment_territory(mouse_position):
        return True
    return False


def check_if_territory_crowded(mouse_position, current_button, deployment):
    new_deployment_stats = deploy_troop_to_territory(mouse_position, current_button)
    return check_if_crowded_in_territory(deployment, new_deployment_stats)


def check_if_crowded_in_territory(deployment_list, new_deployment_stats):
    if len(deployment_list) > 0:
        for deployment in deployment_list:
            if deployment[0] == new_deployment_stats[0] and deployment[2] == new_deployment_stats[2]:
                return True
    return False


def is_mouse_on_deployment_territory(mouse_position):
    if mouse_position[1] > 180 and mouse_position[0] < 360:
        return True
    else:
        return False
