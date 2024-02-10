import general_functions.colors as cl
import general_functions.pygame_functions as pyf
import strategy_choice.strategy_choice_constants as const
import pygame

WIDTH, HEIGHT, FPS = const.get_constants()


def draw_everything_in_strategy_choice_stage(screen, mouse_location):
    screen.fill(cl.BLUE)
    draw_background(screen)
    # draw_unit_deployment_text(screen)
    # draw_deployment_buttons(current_button, screen)
    # draw_deployment(deployment, screen)
    pyf.draw_mouse(screen, mouse_location)


def draw_background(screen):
    starting_y = 180
    draw_background_rectangle(screen, starting_y)
    draw_background_lines(screen, starting_y)


def draw_background_rectangle(screen, starting_y):
    pygame.draw.rect(screen, cl.GREEN, (0, starting_y, 720, 360))  # (x, y, width, height)
    pygame.draw.rect(screen, cl.DARK_RED, (360, starting_y, 720, 360))  # (x, y, width, height)


def draw_background_lines(screen, starting_y):
    for i in range(5):
        if (120 + i * 120) < 360:
            color = cl.DARK_BROWN
            size = 2
        elif (120 + i * 120) == 360:
            color = cl.BLACK
            size = 5
        else:
            color = cl.VERY_DARK_RED
            size = 2
        pygame.draw.line(screen, color, (120 + 120 * i, starting_y), (120 + 120 * i, HEIGHT),
                         size)  # (start_pos), (end_pos), width
