import unittest

from game.components.cell import Cell


class TestCell(unittest.TestCase):
    def test_constructor(self):
        self.cell = Cell("cell_id")
        self.assertEqual(self.cell.id, "cell_id")
        self.assertEqual(len(self.cell.perceptions), 0)


class TestObjects(TestCell):
    def test_set_gold(self):
        raise Exception('Test not implemented yet')

    def test_set_well(self):
        raise Exception('Test not implemented yet')


class TestSetPerceptions(TestCell):
    def test_set_perceive_wumpus(self):
        raise Exception('Test not implemented yet')

    def test_set_perceive_wumpus_odor(self):
        raise Exception('Test not implemented yet')

    def test_set_perceive_gold(self):
        raise Exception('Test not implemented yet')

    def test_set_perceive_breeze(self):
        raise Exception('Test not implemented yet')

    def test_set_perceive_wall(self):
        raise Exception('Test not implemented yet')


class TestPerceptionsSingle(TestSetPerceptions):
    def test_perceive_wumpus(self):
        raise Exception('Test not implemented yet')

    def test_perceive_wumpus_odor(self):
        raise Exception('Test not implemented yet')

    def test_perceive_gold(self):
        raise Exception('Test not implemented yet')

    def test_perceive_breeze(self):
        raise Exception('Test not implemented yet')

    def test_perceive_wall(self):
        raise Exception('Test not implemented yet')

class TestPerceptionsVarious(TestPerceptionsSingle):
    def test_perceive_wumpus_odor_gold(self):
        raise Exception('Test not implemented yet')

    def test_perceive_wumpus_gold(self):
        raise Exception('Test not implemented yet')

    def test_perceive_wumpus_odor_breeze(self):
        raise Exception('Test not implemented yet')

    def test_perceive_wumpus_odor_wall(self):
        raise Exception('Test not implemented yet')

    def test_perceive_wumpus_breeze(self):
        raise Exception('Test not implemented yet')

    def test_perceive_wumpus_wall(self):
        raise Exception('Test not implemented yet')


if __name__ == '__main__':
    unittest.main()
