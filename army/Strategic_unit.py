import army.Unit as unit


class Strategic_unit(unit.Unit):
    def __init__(self, unit_data):
        super(Strategic_unit, self).__init__(unit_data)
        self.target = None

    def attack_target(self):
        self.current_command = "attack_target"

    def get_target(self, target):
        self.target = target
