import pygame

WHITE = (255, 255, 255)


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


def user_choice_events():
    # Event handling
    running = True
    did_user_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            did_user_click = True
    return running, did_user_click


def draw_mouse(screen, mouse_location):
    pygame.draw.circle(screen, WHITE, (mouse_location[0], mouse_location[1]), 2)
    pygame.mouse.set_visible(False)


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return [mouse_x, mouse_y]
