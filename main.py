import pygame
import sys
import unit_choice.unit_choice_screen as ucs

chosen_units = ucs.show_unit_choice_screen()
print(chosen_units)

# Quit Pygame
pygame.quit()
sys.exit()
