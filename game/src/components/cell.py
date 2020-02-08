from game.src.components.enumerations import Object, Perception


class Cell:
    def __init__(self, id):
        self.id = id
        self.object = None
        self.perceptions = set()

    def set_object(self, object: Object):
        self.object = object

    def add_perception(self, perception: Perception):
        self.perceptions.add(perception)
