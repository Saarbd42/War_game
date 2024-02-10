import army.Ground_unit as g_unit


class Infantry(g_unit.Ground_unit):
    def __init__(self, unit_data):
        super(Infantry, self).__init__(unit_data)
        self.life = 100

    def how_much_dmg(self, enemy_unit):
        if enemy_unit.type == "Anti-tank":
            return self.dmg * 2

        elif enemy_unit.type == "Tanks":
            return self.dmg / 2