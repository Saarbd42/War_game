import army.Ground_unit as g_unit


class Air_defence(g_unit.Ground_unit):
    def __init__(self, unit_data):
        super(Air_defence, self).__init__(unit_data)
        self.life = 30

    def how_much_dmg(self, enemy_unit):
        if enemy_unit.type == "Air-force":
            return self.dmg
        return 0