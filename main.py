import pygame
import sys
import unit_choice.unit_choice_screen as ucs
import unit_deployment.unit_deployment_screen as uds

player_chosen_units = ucs.show_unit_choice_screen()
# IF YOU HAVE SPIES -> SEE WHAT THE ENEMY HAVE
player_unit_deployment, player_non_deployable_units = uds.show_unit_deployment_screen(player_chosen_units)
# START THE ACTUAL GAME


# FOR TESTING ONLY
###################################
print(player_unit_deployment)
print(player_non_deployable_units)
####################################

pygame.quit()
sys.exit()
