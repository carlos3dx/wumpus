import unittest

from game.src.components.enumerations import Perception, Object
from game.src.components.wumpus import Wumpus
from game.src.engine.init_board import create_board

rows = 8
cols = 5
pits = 6


class TestInitBoard(unittest.TestCase):
    def setUp(self):
        self.board = create_board(cols, rows, pits)

    def test_walls(self):
        for x in range(cols):
            for y in range(rows):
                if x == 0 or x == cols - 1 or y == 0 or y == rows - 1:
                    self.assertTrue(Perception.WALL in self.board.cells[x][y].perceptions)
                else:
                    self.assertFalse(Perception.WALL in self.board.cells[x][y].perceptions)


class TestPits(TestInitBoard):
    def test_initial_cell_no_pit(self):
        cell = create_board(cols, rows, cols * rows - 2).cells[0][0]
        self.assertIsNot(cell.object, Object.PIT, "There shouldn't ber a pit at initial cell")

    def test_number_pits(self):
        cells = self.board.cells
        pit_counter = 0
        for x in range(cols):
            for y in range(rows):
                if Object.PIT == cells[x][y].object:
                    pit_counter += 1
        self.assertEqual(pit_counter, pits)

    def test_perception_pits(self):
        cells = self.board.cells
        for x in range(cols):
            for y in range(rows):
                if Object.PIT == cells[x][y].object:
                    self.validate_perception_surrounding_pit(cells, x, y)

    def validate_perception_surrounding_pit(self, cells, x, y):
        for i in [x - 1, x + 1]:
            self.validate_perception_pit(cells, i, y)
        for j in [y - 1, y + 1]:
            self.validate_perception_pit(cells, x, j)

    def validate_perception_pit(self, cells, x, y):
        if x in range(cols) and y in range(rows):
            self.assertTrue(Perception.BREEZE in cells[x][y].perceptions, f'Expected breeze at {x}x{y}')


class TestGoldBar(TestInitBoard):
    def test_only_one_gold_bar(self):
        cells = self.board.cells
        gold_bars = 0
        for x in range(cols):
            for y in range(rows):
                if Object.GOLD == cells[x][y].object:
                    gold_bars += 1
        self.assertEqual(gold_bars, 1, "There should be only one gold bat at the board")

    def test_gold_pit_collision(self):
        cells = create_board(cols, rows, cols * rows - 2).cells
        gold_bars = 0
        pit_counter = 0
        for x in range(cols):
            for y in range(rows):
                if Object.GOLD == cells[x][y].object:
                    gold_bars += 1
                elif Object.PIT == cells[x][y].object:
                    pit_counter += 1
        self.assertTrue(gold_bars == 1 and pit_counter == cols * rows - 2,
                        "Gold bar and pit shouldn't be placed at the same cell")


class TestWumpusLocation(TestInitBoard):
    def test_wumpus_location(self):
        wumpus = Wumpus()
        create_board(cols, rows, cols * rows - 2, wumpus)
        pos = wumpus.position
        self.assertFalse(pos.x == 0 and pos.y == 0, 'Wumpus cannot be initialized at 0x0')

    def test_wumpous_pit_collision(self):
        wumpus = Wumpus()
        cells = create_board(cols, rows, cols * rows - 2, wumpus).cells
        pos = wumpus.position
        self.assertFalse(cells[pos.x][pos.y] == Object.PIT, "Wumpus cannot be placed at a cell with a pit")


if __name__ == '__main__':
    unittest.main()
