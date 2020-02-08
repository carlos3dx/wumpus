from game.src.components.cell import Cell


class Board:
    def __init__(self, cols, rows):
        self.cells = [[Cell(f'{i}x{j}') for j in range(rows)] for i in range(cols)]
