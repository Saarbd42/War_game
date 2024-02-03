import pygame
import Deployment_button as dbt

def get_deployment_button_list(player_chosen_units):
    dep_button_list = pygame.sprite.Group()
    origin_button_list = get_deployment_buttons(player_chosen_units)
    for button in origin_button_list:
        dep_button_list.add(button)
    return dep_button_list


def get_deployment_buttons(player_chosen_units):
    button_list = []
    # for i in range(len(player_chosen_units)):
        # string =
        # dbt.Deployment_button([40, 100], )
    return []

# def get_picture_path()