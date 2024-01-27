import pygame
import button as bt
import images_functions as imf

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (129, 127, 38)


def get_button_list():
    button_list = pygame.sprite.Group()
    infantry_button = bt.Button([100, 100], ["sprites/infantry.png", "sprites/infantry_blue_mark.png"], "infantry")
    button_list.add(infantry_button)
    return button_list


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return [mouse_x, mouse_y]


def button_collision_test(button_list, mouse_position, did_user_click):
    for button in button_list:
        button.check_mouse_collision(mouse_position[0], mouse_position[1], did_user_click)
    return button_list


def draw_everything_in_unit_choice_stage(screen, button_list, mouse_location):
    screen.fill(BLACK)
    button_list.draw(screen)
    draw_unit_choice_text(screen)
    draw_mouse(screen, mouse_location)


def draw_mouse(screen, mouse_location):
    pygame.draw.circle(screen, WHITE, (mouse_location[0], mouse_location[1]), 3)
    pygame.mouse.set_visible(False)


def draw_unit_choice_text(screen):
    title_text, title_rect = imf.get_text_stats("Please pick 4 units", 42, WHITE, [300, 50])
    imf.draw_titles(screen, [title_text, title_rect])
