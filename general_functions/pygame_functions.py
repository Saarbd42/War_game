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
