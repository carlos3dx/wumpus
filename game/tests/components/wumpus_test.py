import unittest

from game.components.wumpus import Wumpus


class TestWumpus(unittest.TestCase):
    def setUp(self):
        self.wumpus = Wumpus()

    def test_sconstructor(self):
        self.assertEqual(self.wumpus, "Wumpus")

    def test_yell_(self):
        raise Exception('Test not implemented yet')



if __name__ == '__main__':
    unittest.main()
