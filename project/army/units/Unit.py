class Unit:
    def __init__(self, name):
        self.name = name
        self.life = self.get_initial_data()[0]
        self.atk_dmg = self.get_initial_data()[0]
        self.def_dmg = self.get_initial_data()[0]
        self.current_command = None

    def get_initial_data(self):
        return [0, 0, 0]
