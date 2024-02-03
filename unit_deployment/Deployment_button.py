import pygame


class Deployment_button(pygame.sprite.Sprite):
    def __init__(self, location, picture_path, unit_type):
        super(Deployment_button, self).__init__()

        # picture path
        self.picture_path = picture_path

        # current image
        self.color_key = (163, 73, 164)
        self.image = pygame.image.load(picture_path).convert()
        self.image.set_colorkey(self.color_key)

        # image size
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        # clicked
        self.clicked = False

        # unit
        self.unit_type = unit_type
        self.unit_type = unit_type

