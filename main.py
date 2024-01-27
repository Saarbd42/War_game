import pygame
import sys
import constants as const
import pygame_functions as pyf
import unit_choice_functions as ucf

# Constants
WIDTH, HEIGHT, FPS = const.get_constants()
# BLACK, WHITE, LIGHT_RED, BROWN = const.get_colors()

# Initialize Pygame
screen, clock = pyf.initiate_pygame(WIDTH, HEIGHT)

# Define buttons
button_list = ucf.get_button_list()

# Game loop
running = True
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

    # Draw everything
    ucf.draw_everything_in_unit_choice_stage(screen, button_list, mouse_position)

    # Update the display
    clock = pyf.update_frame(clock, FPS)

# Quit Pygame
pygame.quit()
sys.exit()
