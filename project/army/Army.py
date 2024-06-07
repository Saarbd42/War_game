
class Army:
    def __init__(self, unit_choices):
        self.units = self.build_army(unit_choices)
        self.territory = 3
        self.factories = 8

    def build_army(self, unit_choices):
        return