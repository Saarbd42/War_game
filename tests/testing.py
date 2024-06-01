import random
from project.Unit_choice_screen import Unit_choice_screen
import sys

user_choice_screen = Unit_choice_screen()
chosen_units = user_choice_screen.start_screen_loop()
print(chosen_units)