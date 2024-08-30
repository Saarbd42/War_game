import pygame
import project.config as cnf
from project.base_classes.Button_collisions import ButtonCollisions


# BUTTON CLASS HOLDS THE POSITION
class Button(pygame.sprite.Sprite):
    def __init__(self, location, picture_paths, unit):
        super(Button, self).__init__()

        # Picture path
        self.normal_picture_path = picture_paths[0]
        self.chosen_picture_path = picture_paths[1]

        # Current Image
        self.image = pygame.image.load(picture_paths[0]).convert()
        self.image.set_colorkey(cnf.COLOR_KEY)

        # Image Size
        self.rect = self.image.get_rect()
        self.update_rect_according_to_location(location)

        # Button Collisions
        self.button_collisions = ButtonCollisions(self.rect)
        self.clicked = False

        self.unit = unit

    def check_mouse_collision(self, mouse_x, mouse_y, user_clicked):
        if self.button_collisions.check_if_user_clicked_button(mouse_x, mouse_y, user_clicked):
            self.change_button_clicked_status()
        self.change_button_picture_according_user_actions(mouse_x, mouse_y)

    def change_button_clicked_status(self):
        if not self.clicked:
            self.clicked = True
        else:
            self.clicked = False

    def change_button_picture_according_user_actions(self, mouse_x, mouse_y):
        if self.button_collisions.check_if_mouse_xy_matches_button_xy(mouse_x, mouse_y) \
                or self.clicked:
            self.set_picture(self.chosen_picture_path)
        else:
            self.set_picture(self.normal_picture_path)

    def set_picture(self, picture_path):
        self.image = pygame.image.load(picture_path).convert()
        self.image.set_colorkey(cnf.COLOR_KEY)

    def update_rect_according_to_location(self, location):
        self.rect.x = location[0]
        self.rect.y = location[1]
