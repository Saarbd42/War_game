from project.army.Army_builder import ArmyBuilder
from project.Single_turn_logic import SingleTurnLogic


class Game_manager:
    def __init__(self):
        self.army_builder = ArmyBuilder()
        self.single_turn = SingleTurnLogic()
        self.armies = None

    def start_game_loop(self):
        self.armies = self.army_builder.build_armies()
        end = False
        while not end:
            end, self.armies = self.single_turn.play_a_single_turn(self.armies)