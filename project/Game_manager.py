from project.unit_choice.Unit_choice_screen import Unit_choice_screen
import project.enemy_unit_choice.enemy_unit_choice_functions as ecf


# enemy_chosen_units = ecf.get_iranian_proxy()

class Game_manager:
    def __init__(self):
        self.unit_choice_screen = Unit_choice_screen()

    def start_game_loop(self):
        self.build_armies()
        end = False
        while not end:
            self.make_war_decision()
            end = self.get_turn_results()

    def build_armies(self):
        chosen_units = self.unit_choice_screen.start_screen_loop()
        print(chosen_units)
        return

    def make_war_decision(self):
        # Civilian screen
        # spies
        # Land Forces (+Artillery)
        # Air Forces
        # Missiles
        # Air-defence
        # Cyber
        # Enemy Decisions
        return

    def get_turn_results(self):
        end, results = self.calculate_turn_results()
        self.show_turn_results(results)
        return end

    def show_turn_results(self, results):
        return

    def calculate_turn_results(self):
        return True, ["STUFF"]
