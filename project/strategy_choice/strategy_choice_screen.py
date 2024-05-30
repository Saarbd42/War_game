import project.strategy_choice.strategy_choice_constants as const
import project.general_functions.pygame_functions as pyf
import project.strategy_choice.strategey_choice_drawing_functions as sdf


def show_strategy_screen(player_army, enemy_army):
    # Constants
    WIDTH, HEIGHT, FPS = const.get_constants()

    # Initialize Pygame
    screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)

    basic_variables = [screen, clock, FPS]
    armies = [player_army, enemy_army]

    return unit_strategy_game_loop(basic_variables, armies)


def unit_strategy_game_loop(basic_variables, armies):
    screen, clock, FPS = unpack_basic_variables(basic_variables)
    running = True

    while running:
        mouse_position, did_user_click, running = pyf.get_user_input()

        # Game logic

        # Draw everything and update the display
        sdf.draw_everything_in_strategy_choice_stage(screen, mouse_position, armies)
        clock = pyf.update_frame(clock, FPS)


def unpack_basic_variables(basic_variables):
    return basic_variables[0], basic_variables[1], basic_variables[2]
