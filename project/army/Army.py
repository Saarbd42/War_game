from project.army.units.all_units import ALL_UNITS_DICTS
from project.army.units.Unit import Unit


class Army:
    def __init__(self, unit_choices):
        self.units = self.build_army(unit_choices)
        self.territory = 3
        self.factories = 8

    def get_army_units_names(self):
        name_list = []
        for unit in self.units:
            name_list.append(unit.name)
        return name_list

    @staticmethod
    def build_army(unit_choices):
        army_units = []
        for unit_name in unit_choices:
            for dict in ALL_UNITS_DICTS:
                if unit_name == dict["name"]:
                    army_units.append(Unit(dict))
        return army_units

