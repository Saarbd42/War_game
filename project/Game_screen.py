import pygame
import project.unit_choice.unit_choice_constants as const
import project.general_functions.pygame_functions as pyf


class Game_screen:
    def __init__(self):
        self.width, self.height, self.fps = const.get_constants()

    def start_screen_loop(self, current_game_state=None):
        # Initialize Pygame
        screen, clock = pyf.initiate_pygame(self.width, self.height)

        running = True

        # Game loop
        while running:
            mouse_position = self.get_mouse_position()
            running, did_user_click = self.user_choice_events()

            current_game_state = self.screen_logic(current_game_state)

            clock = pyf.update_frame(clock, self.fps)

    def screen_logic(self, current_game_state):
        return None

    def user_choice_events(self):
        # Event handling
        running = True
        did_user_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                did_user_click = True
        return running, did_user_click

    def get_mouse_position(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return [mouse_x, mouse_y]
