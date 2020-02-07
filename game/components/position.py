class Position:
    directions = ["N", "E", "S", "W"]

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation % 4

    def turn(self, direction):
        self.orientation = (self.orientation + direction) % 4

    def turn_left(self):
        self.turn(-1)

    def turn_right(self):
        self.turn(1)

    def move_forward(self):
        pass
