import pygame


def initiate_pygame(WIDTH, HEIGHT):
    # Initialize Pygame
    pygame.init()
    # Create the game window
    pygame.display.set_caption("War game")
    return initiate_pygame_objects(WIDTH, HEIGHT)


def initiate_pygame_objects(WIDTH, HEIGHT):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock


def update_frame(clock, FPS):
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
    return clock


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return [mouse_x, mouse_y]

