from project.game_management.Player_decision_maker import PlayerDecisionMaker


class SingleTurnLogic:
    def __init__(self):
        self.player_decision_maker = PlayerDecisionMaker()

    def play_a_single_turn(self, armies):
        player_decisions = self.player_decision_maker.player_make_war_decision(armies)
        enemy_decisions = ""  # ENEMY DECISIONS
        new_armies = ""  # UPDATE ARMIES
        results = ""  # SHOW RESULTS
        end = True  # CHECK IF THE GAME ENDED
        return end, new_armies
