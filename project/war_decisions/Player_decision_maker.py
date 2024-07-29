from project.war_decisions.passive_screens.spies_screen import SpiesScreen
from project.war_decisions.passive_screens.player_units_screen import PlayerUnitsScreen


class PlayerDecisionMaker:
    def __init__(self):
        self.name = "PlayerDecisionMaker"

    def player_make_war_decision(self, armies):
        player_decisions = []
        self.show_passive_screens(armies)

        # Land Forces (+Artillery)
        # Air Forces
        # Missiles
        # Air-defence
        # Cyber
        # Enemy Decisions
        return player_decisions  # TODO: CHANGE THAT

    @staticmethod
    def show_passive_screens(armies):
        player_units_screen = PlayerUnitsScreen(armies[0], armies[1])
        player_units_screen.start_screen_loop()

        spies_screen = SpiesScreen(armies[0], armies[1])
        if "Spies" in armies[0].get_army_units_names():
            spies_screen.start_screen_loop()
