from random import seed, randint

from game.src.components.board import Board
from game.src.components.enumerations import Perception, Object
from game.src.components.wumpus import Wumpus


def create_board(x, y, pits, wumpus=Wumpus()):
    board = Board(x, y)
    set_walls(board, x, y)
    set_pits(board, x, y, pits)
    set_gold_bar(board, x, y)
    set_wumpus_location(board, x, y, wumpus)
    return board


def get_random_cell(board, max_x, max_y):
    x, y = get_random_coords(max_x, max_y)
    return board.cells[x][y]


def get_random_coords(max_x, max_y):
    seed()
    x = randint(0, max_x - 1)
    y = randint(0, max_y - 1)
    return x, y


def set_walls(board, x, y):
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1 or j == 0 or j == y - 1:
                board.cells[i][j].add_perception(Perception.WALL)


def set_pits(board, max_x, max_y, pits):
    for pit in range(pits):
        cell = get_random_cell(board, max_x, max_y)
        while cell.object is not None or cell.id == "0x0":
            cell = get_random_cell(board, max_x, max_y)
        cell.object = Object.PIT
        set_perception_near(board, cell, max_x, max_y, Perception.BREEZE)


def set_perception_near(board, cell, max_x, max_y, perception):
    x, y = [int(val) for val in cell.id.split("x")]
    for i in [x - 1, x + 1]:
        set_perception(board, i, y, max_x, max_y, perception)
    for j in [y - 1, y + 1]:
        set_perception(board, x, j, max_x, max_y, perception)


def set_perception(board, x, y, max_x, max_y, perception):
    if x in range(max_x) and y in range(max_y):
        board.cells[x][y].add_perception(perception)


def set_gold_bar(board, max_x, max_y):
    cell = get_random_cell(board, max_x, max_y)
    while cell.object is not None and cell.object is Object.PIT:
        cell = get_random_cell(board, max_x, max_y)
    cell.set_object(Object.GOLD)
    cell.add_perception(Perception.GOLD)


def set_wumpus_location(board, max_x, max_y, wumpus):
    cell = get_random_cell(board, max_x, max_y)
    while cell.object is Object.PIT or cell.id == "0x0":
        cell = get_random_cell(board, max_x, max_y)
    x, y = [int(val) for val in cell.id.split("x")]
    wumpus.set_position(x, y, randint(0, 3))
    cell.add_perception(Perception.WUMPUS)
    set_perception_near(board, cell, max_x, max_y, Perception.WUMPUS_ODOR)


