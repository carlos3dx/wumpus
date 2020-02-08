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


def refresh_board(game):
    board = game.board
    if game.player.has_gold:
        remove_perception(board, Perception.GOLD)
    remove_perception(board, Perception.WUMPUS)
    remove_perception(board, Perception.WUMPUS_ODOR)
    if game.wumpus is not None:
        wumpus = game.wumpus
        cell = board.cells[wumpus.position.x][wumpus.position.y]
        cell.add_perception(Perception.WUMPUS)
        set_perception_near(board, cell, len(board.cells), len(board.cells[0]), Perception.WUMPUS_ODOR)


def get_random_cell(board):
    max_cols = len(board.cells[0])
    max_rows = len(board.cells)
    col, row = get_random_coords(max_cols, max_rows)
    return board.cells[row][col]


def get_random_coords(max_cols, max_rows):
    seed()
    col = randint(0, max_cols - 1)
    row = randint(0, max_rows - 1)
    return col, row


def set_walls(board):
    cols = len(board.cells[0])
    rows = len(board.cells)
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


def check_pit(game):
    p_x = game.player.position.x
    p_y = game.player.position.y
    if game.board.cells[p_x][p_y].object == Object.PIT:
        print("You should be more careful, you stepped on an endless pit")
        print("G A M E   O V E R")
        exit(0)


def remove_perception(board, perception):
    cells = board.cells
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            cell = cells[i][j]
            if perception in cell.perceptions:
                cell.perceptions.remove(perception)
