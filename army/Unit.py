class Unit():
    def __init__(self, unit_data):

        # Position and type
        self.x_position = unit_data[0]
        self.type = unit_data[1]
        self.y_position = unit_data[2]

        # Data
        self.exposed = False
        self.dead = False
        self.life = 100
        self.dmg = 20

        # Strategy
        self.current_command = None

    def take_dmg(self, dmg):
        self.life -= dmg

    def check_if_dead(self):
        if self.life <= 0:
            self.dead = True

    def check_if_exposed(self, enemy_army):
        if enemy_army.spies or self.check_if_close_to_enemy(enemy_army):
            self.exposed = True
        else:
            self.exposed = False

    def check_if_close_to_enemy(self, enemy_army):
        for enemy_unit in enemy_army.unit_list:
            if self.check_if_enemy_unit_close(enemy_unit):
                return True
        return False

    def check_if_enemy_unit_close(self, enemy_unit):
        if enemy_unit.x_position - 1 == self.x_position or enemy_unit.x_position == self.x_position or enemy_unit.x_position + 1 == self.x_position:
            return True

    def reset_command(self):
        self.current_command = None
