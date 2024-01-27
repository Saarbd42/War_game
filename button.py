import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, location, picture_paths, unit):
        super(Button, self).__init__()

        # picture path
        self.normal_picture_path = picture_paths[0]
        self.chosen_picture_path = picture_paths[1]

        # current image
        self.image = pygame.image.load(picture_paths[0]).convert()
        self.image.set_colorkey((0, 0, 0))

        # image size
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        # clicked
        self.clicked = False

    def check_mouse_collision(self, mouse_x, mouse_y, user_clicked):
        self.check_if_user_clicked_button(mouse_x, mouse_y, user_clicked)
        self.change_button_picture_according_user_actions(mouse_x, mouse_y)

    def check_if_user_clicked_button(self, mouse_x, mouse_y, user_clicked):
        if self.check_if_mouse_xy_matches_button_xy(mouse_x, mouse_y) and \
                user_clicked:
            self.change_button_clicked_status()

    def change_button_clicked_status(self):
        if not self.clicked:
            self.clicked = True
        else:
            self.clicked = False

    def change_button_picture_according_user_actions(self, mouse_x, mouse_y):
        if self.check_if_mouse_xy_matches_button_xy(mouse_x, mouse_y) or self.clicked:
            self.set_picture(self.chosen_picture_path)
        else:
            self.set_picture(self.normal_picture_path)

    def set_picture(self, picture_path):
        self.image = pygame.image.load(picture_path).convert()
        self.image.set_colorkey((0, 0, 0))

    def check_if_mouse_xy_matches_button_xy(self, mouse_x, mouse_y):
        if self.check_if_mouse_x_matches_button_x(mouse_x) and \
                self.check_if_mouse_y_matches_button_y(mouse_y):
            return True

    def check_if_mouse_x_matches_button_x(self, mouse_x):
        if self.rect.x < mouse_x < (self.rect.x + self.rect.width):
            return True

    def check_if_mouse_y_matches_button_y(self, mouse_y):
        if self.rect.y < mouse_y < (self.rect.y + self.rect.height):
            return True
