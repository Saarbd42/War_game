import pygame
import project.unit_choice.unit_choice_constants as const
import project.general_functions.pygame_functions as pyf


class Game_screen:
    def __init__(self):
        self.width, self.height, self.fps = const.get_constants()
        self.mouse_position = None
        self.current_game_state = None

    def start_screen_loop(self):
        screen, clock = pyf.initiate_pygame(self.width, self.height)
        running = True
        while running:
            running = self.screen_logic()
            self.draw_everything(screen)
            clock = pyf.update_frame(clock, self.fps)
        return self.current_game_state

    def screen_logic(self):
        running, did_user_click = self.user_choice_events()
        self.mouse_position = self.get_mouse_position()
        return running

    def update_current_game_state(self, new_game_state):
        self.current_game_state = new_game_state

    def draw_everything(self, screen):
        return

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
