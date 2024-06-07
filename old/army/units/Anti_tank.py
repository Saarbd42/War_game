import project.army.Ground_unit as g_unit


class Anti_tank(g_unit.Ground_unit):
    def __init__(self, unit_data):
        super(Anti_tank, self).__init__(unit_data)
        self.life = 100

    def how_much_dmg(self, enemy_unit):
        if enemy_unit.type == "Tanks":
            return self.dmg * 2

        elif enemy_unit.type == "Infantry":
            return self.dmg / 2