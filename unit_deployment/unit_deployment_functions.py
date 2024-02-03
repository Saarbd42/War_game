import pygame
import general_functions.images_functions as imf

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (129, 127, 38)
DARK_BROWN = (89, 59, 42)
LIGHT_BLUE = (0, 162, 232)
BLUE = (63, 72, 204)
DARK_GREY = (90, 90, 90)
GREY = (160, 160, 160)
GREEN = (34, 177, 76)


def draw_everything_in_unit_deployment_stage(screen, mouse_location):
    screen.fill(BLUE)
    draw_background(screen)
    draw_unit_deployment_text(screen)
    draw_mouse(screen, mouse_location)


def draw_unit_deployment_text(screen):
    draw_the_head_line(screen)


def draw_the_head_line(screen):
    title_text, title_rect = imf.get_text_stats("Deploy your units", 60, WHITE, [360, 40])
    imf.draw_titles(screen, [title_text, title_rect])


def draw_background(screen):
    starting_y = 180
    draw_background_rectangle(screen, starting_y)
    draw_background_lines(screen, starting_y)


def draw_background_rectangle(screen, starting_y):
    pygame.draw.rect(screen, GREEN, (0, starting_y, 720, 360))  # (x, y, width, height)
    pygame.draw.rect(screen, GREY, (360, starting_y, 720, 360))  # (x, y, width, height)


def draw_background_lines(screen, starting_y):
    for i in range(5):
        if (120 + i * 120) < 360:
            pygame.draw.line(screen, DARK_BROWN, (120 + 120 * i, starting_y), (120 + 120 * i, 360),
                             5)  # (start_pos), (end_pos), width
        else:
            pygame.draw.line(screen, DARK_GREY, (120 + 120 * i, starting_y), (120 + 120 * i, 360),
                             5)  # (start_pos), (end_pos), width


def draw_mouse(screen, mouse_location):
    pygame.draw.circle(screen, WHITE, (mouse_location[0], mouse_location[1]), 2)
    pygame.mouse.set_visible(False)
