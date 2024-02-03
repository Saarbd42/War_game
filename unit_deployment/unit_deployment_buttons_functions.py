import pygame
import unit_choice.button as bt


def get_next_button(player_chosen_units):
    string = get_sprite_paths(player_chosen_units[0])
    new_button = bt.Button([50, 30], string, player_chosen_units[0])
    player_chosen_units = player_chosen_units[1:]
    return player_chosen_units, new_button


def get_sprite_paths(sprite_name):
    string = ["sprites/" + str(sprite_name) + ".png",
              "sprites/" + str(sprite_name) + "_blue_mark.png"]
    return string
