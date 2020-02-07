from game.components.position import Position


class Character:
    def __init__(self, name, pos_x=0, pos_y = 0, orientation = 0):
        self.position = Position(pos_x, pos_y, orientation)
        self.name = name

