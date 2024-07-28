from project.war_decisions.unit_decision_screens.spies_screen import SpiesScreen
from project.army.ArmyBuilder import ArmyBuilder


class Game_manager:
    def __init__(self):
        self.army_builder = ArmyBuilder()
        self.armies = None

    def start_game_loop(self):
        self.armies = self.army_builder.build_armies()
        end = False
        while not end:
            player_decisions = self.player_make_war_decision()
            enemy_decisions = ""  # TODO: ADD ENEMY LOGIC
            end = self.get_turn_results()

    def player_make_war_decision(self):
        player_units = self.armies[0].get_army_units_names()
        player_decisions = []
        # Civilian screen
        spies_screen = SpiesScreen(self.armies[0], self.armies[1])
        if "Spies" in player_units:
            spies_screen.start_screen_loop()
        # Land Forces (+Artillery)
        # Air Forces
        # Missiles
        # Air-defence
        # Cyber
        # Enemy Decisions
        return ""  # TODO: CHANGE THAT

    def get_turn_results(self):
        end, results = self.calculate_turn_results()
        self.show_turn_results(results)
        return end

    def show_turn_results(self, results):
        return

    def calculate_turn_results(self):
        return True, ["STUFF"]
