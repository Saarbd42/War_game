import pygame
import sys
import unit_choice.unit_choice_screen as ucs
import unit_deployment.unit_deployment_screen as uds
player_chosen_units = ucs.show_unit_choice_screen()
player_unit_deployment = uds.show_unit_deployment_screen(player_chosen_units)

# Quit Pygame
pygame.quit()
sys.exit()
