import pygame
import general_functions.images_functions as imf
import unit_deployment.unit_deployment_constants as const
import general_functions.colors as cl

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (129, 127, 38)
DARK_BROWN = (89, 59, 42)
LIGHT_BLUE = (0, 162, 232)
BLUE = (63, 72, 204)
DARK_GREY = (90, 90, 90)
GREY = (160, 160, 160)
GREEN = (34, 177, 76)
DARK_RED = (136, 0, 21)
VERY_DARK_RED = (77, 0, 12)
WIDTH, HEIGHT, FPS = const.get_constants()


def draw_everything_in_unit_deployment_stage(screen, mouse_location, current_button, deployment):
    screen.fill(BLUE)
    draw_background(screen)
    draw_unit_deployment_text(screen)
    draw_deployment_buttons(current_button, screen)
    draw_deployment(deployment, screen)
    draw_mouse(screen, mouse_location, current_button)


def draw_deployment(deployment, screen):
    if len(deployment) > 0:
        for unit_data in deployment:
            unit_image, unit_rect = get_deployed_unit_details(unit_data)
            screen.blit(unit_image, unit_rect)


def get_deployed_unit_details(unit_data):
    unit_image = get_deployed_unit_image(unit_data)
    unit_rect = get_deployed_unit_rect(unit_data, unit_image)
    return unit_image, unit_rect


def get_deployed_unit_image(unit_data):
    unit_path = 'sprites/' + str(unit_data[1]) + '.png'
    unit_image = pygame.image.load(unit_path)
    unit_image.set_colorkey((163, 73, 164))
    return unit_image


def get_deployed_unit_rect(unit_data, unit_image):
    unit_rect = unit_image.get_rect()
    unit_rect.x = 20 + (unit_data[0] - 1) * 120
    unit_rect.y = 150 + (unit_data[2]) * 60
    return unit_rect


def draw_deployment_buttons(current_button, screen):
    if not current_button.clicked:
        screen.blit(current_button.image, current_button.rect)
        return True
    else:
        return False


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
    pygame.draw.rect(screen, cl.GREY, (360, starting_y, 720, 360))  # (x, y, width, height)


def draw_background_lines(screen, starting_y):
    for i in range(5):
        if (120 + i * 120) < 360:
            color = DARK_BROWN
            size = 2
        elif (120 + i * 120) == 360:
            color = BLACK
            size = 5
        else:
            color = cl.DARK_GREY
            size = 2

        pygame.draw.line(screen, color, (120 + 120 * i, starting_y), (120 + 120 * i, HEIGHT),
                         size)  # (start_pos), (end_pos), width


def draw_mouse(screen, mouse_location, current_button):
    if current_button.clicked:
        adjusted_mouse_location = [mouse_location[0] - 32, mouse_location[1] - 32]
        screen.blit(current_button.image, adjusted_mouse_location)
    else:
        pygame.draw.circle(screen, WHITE, (mouse_location[0], mouse_location[1]), 2)
    pygame.mouse.set_visible(False)
