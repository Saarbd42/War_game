import army.Unit as unit


class Ground_unit(unit.Unit):
    def __init__(self, unit_data):
        super(Ground_unit, self).__init__(unit_data)

    def move_forward(self):
        self.current_command = "forward"

    def move_backward(self):
        self.current_command = "backward"

    def stand_your_ground(self):
        self.current_command = "defence"
