import pygame
import sys
import constants as const
import pygame_functions as pyf
import unit_choice_functions as ucf

# Constants
WIDTH, HEIGHT, FPS = const.get_constants()

# Initialize Pygame
screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)

# Define buttons
button_list = ucf.get_button_list()

# Game loop
running = True
units_num = 0
while running:

    mouse_position = ucf.get_mouse_position()
    did_user_click = False

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            did_user_click = True

    # Game logic
    button_list = ucf.button_collision_test(button_list, mouse_position, did_user_click)
    if did_user_click:
        units_num = ucf.how_many_more_units_can_the_player_choose(button_list)

    # Draw everything
    ucf.draw_everything_in_unit_choice_stage(screen, button_list, mouse_position)

    # Update the display
    clock = pyf.update_frame(clock, FPS)

    if units_num == 4:
        running = False

# Quit Pygame
pygame.quit()
sys.exit()
