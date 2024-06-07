from project.war_decisions.Decision_choice_screen import DecisionChoiceScreen


class SpiesScreen(DecisionChoiceScreen):
    def __init__(self, player_army, enemy_army):
        super(SpiesScreen, self).__init__(player_army, enemy_army)