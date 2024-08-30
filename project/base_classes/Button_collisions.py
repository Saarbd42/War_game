class ButtonCollisions:
    def __init__(self, rect):
        self.rect = rect

    def check_if_user_clicked_button(self, mouse_x, mouse_y, user_clicked):
        if self.check_if_mouse_xy_matches_button_xy(mouse_x, mouse_y) and \
                user_clicked:
            return True

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
