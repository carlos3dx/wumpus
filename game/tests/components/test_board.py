import unittest

from game.src.components.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 8)

    def test_board_cells(self):
        for i in range(5):
            for j in range(8):
                self.assertEqual(self.board.cells[i][j].id, f'{i}x{j}')


if __name__ == '__main__':
    unittest.main()
