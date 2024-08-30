from project.game_screens.Spies_screen import SpiesScreen
from project.game_screens.Player_units_screen import PlayerUnitsScreen
from project.game_screens.Land_forces_screen import LandForcesScreen
from project.config import LAND_FORCES_NAMES


class PlayerDecisionMaker:
    def __init__(self):
        self.name = "PlayerDecisionMaker"

    def player_make_war_decision(self, armies):
        '''
        :param armies: a list of two armies [player_army, enemy_army]
        :return: player decisions list
        '''
        player_decisions = []
        self.show_passive_screens(armies)
        land_forces_action = self.show_action_choice_screen(armies, LandForcesScreen(armies[0], armies[1]),
                                                            LAND_FORCES_NAMES)
        # Air Forces
        # Missiles
        # Air-defence
        # Cyber
        # Enemy Decisions
        return player_decisions  # TODO: CHANGE THAT

    @staticmethod
    def show_action_choice_screen(armies, screen_type, needed_units):
        screen = screen_type
        for name in needed_units:
            if name in armies[0].get_army_units_names():
                return screen.start_screen_loop()

    @staticmethod
    def show_passive_screens(armies):
        player_units_screen = PlayerUnitsScreen(armies[0], armies[1])
        player_units_screen.start_screen_loop()

        spies_screen = SpiesScreen(armies[0], armies[1])
        if "Spies" in armies[0].get_army_units_names():
            spies_screen.start_screen_loop()
