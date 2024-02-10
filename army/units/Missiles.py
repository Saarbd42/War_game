import army.Strategic_unit as st_unit


class Missiles(st_unit.Strategic_unit):
    def __init__(self, unit_data):
        super(Missiles, self).__init__(unit_data)
        self.life = 100

    def how_much_dmg(self, enemy_unit):
        return self.dmg / 2