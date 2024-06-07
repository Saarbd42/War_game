import pygame


def get_sprite_paths(sprite_name):
    initial_path = r'C:\Users\97252\Desktop\CS\PersonalProjects\War_game\sprites\\'
    string = [initial_path + str(sprite_name) + ".png",
              initial_path + str(sprite_name) + "_blue_mark.png"]
    return string


def draw_titles(screen, title_data):
    # Draw the title text
    screen.blit(title_data[0], title_data[1])


def get_text_stats(text, size, color, position):
    # Create a font for the title
    font = pygame.font.Font(None, size)  # You can adjust the font size and style

    # Create the title text
    title_text = font.render(text, True, color)

    # Position the title text
    title_rect = title_text.get_rect()
    title_rect.center = (position[0], position[1])  # You can adjust the vertical position
    return title_text, title_rect


def get_picture_stats(path, position):
    # Load the custom button image
    image = pygame.image.load(path)

    # Define the button position
    image_x = (position[0] - image.get_width())
    image_y = (position[1] - image.get_height())
    return image, image_x, image_y
