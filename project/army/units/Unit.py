
class Unit:
    def __init__(self, unit_dict):
        self.name = unit_dict["name"]
        self.life = unit_dict["life"]
        self.atk_dmg = unit_dict["attack dmg"]
        self.def_dmg = unit_dict["defense dmg"]
        self.visible = unit_dict["visible"]
        self.ground = unit_dict["ground"]
