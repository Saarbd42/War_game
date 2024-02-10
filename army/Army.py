from army.units.Air_force import Air_force
from army.units.Air_defence import Air_defence
from army.units.Missiles import Missiles
from army.units.Tanks import Tanks
from army.units.Anti_tank import Anti_tank
from army.units.Infantry import Infantry


def get_initial_front_line(enemy_team):
    if enemy_team:
        return 7
    else:
        return 0


class Army():
    def __init__(self, deployable_data_list, non_deployable_data_list, am_i_enemy_team):
        self.unit_list = self.build_an_army(deployable_data_list)
        self.spies = self.check_for_spies(non_deployable_data_list)
        self.cyber = self.check_for_cyber(non_deployable_data_list)
        self.front_line = self.update_front_line(am_i_enemy_team)
        self.communication = True

    def check_which_units_are_exposed(self, enemy_army):
        for unit in self.unit_list:
            unit.check_if_exposed(enemy_army)

    def update_front_line(self, enemy_team):
        front_list = get_initial_front_line(enemy_team)
        if self.check_if_army_exist():
            for unit in self.unit_list:
                front_list = self.check_if_unit_in_front_line(unit, enemy_team, front_list)
        return front_list

    def check_if_army_exist(self):
        if len(self.unit_list) > 0:
            return True
        return False

    def check_if_unit_in_front_line(self, unit, enemy_team, front_list):
        if enemy_team:
            return min(unit.x_position, front_list)
        else:
            return max(unit.x_position, front_list)


    def build_an_army(self, deployable_data_list):
        unit_list = []
        for i in range(len(deployable_data_list)):
            unit_data = deployable_data_list[i]
            unit_list.append(self.get_unit_object(unit_data))
        return unit_list

    def get_unit_object(self, unit_data):
        if unit_data[1] == "Tanks":
            return Tanks(unit_data)
        elif unit_data[1] == "Infantry":
            return Infantry(unit_data)
        elif unit_data[1] == "Anti-tank":
            return Anti_tank(unit_data)
        elif unit_data[1] == "Air-defence":
            return Air_defence(unit_data)
        elif unit_data[1] == "Air-force":
            return Air_force(unit_data)
        elif unit_data[1] == "Missiles":
            return Missiles(unit_data)

    def check_for_spies(self, non_deployable_data_list):
        if "Spies" in non_deployable_data_list:
            return True
        return False

    def check_for_cyber(self, non_deployable_data_list):
        if "Cyber" in non_deployable_data_list:
            return True
        return False

