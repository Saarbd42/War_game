import project.army.Strategic_unit as st_unit


class Air_force(st_unit.Strategic_unit):
    def __init__(self, unit_data):
        super(Air_force, self).__init__(unit_data)
        self.life = 30
        self.dmg = 20

    def protect_the_skies(self):
        self.current_command = "sky_defence"

    def how_much_dmg(self, enemy_unit):
        if self.current_command == "sky_defence":
            return 10
        return self.dmg