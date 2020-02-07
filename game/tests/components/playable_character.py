import unittest

from game.components.playable_character import PlayableCharacter


class TestPlayableCharacter(unittest.TestCase):
    def test_sconstructor_default(self):
        self.pc = PlayableCharacter()
        self.assertEqual(self.pc.name, "Player")


class TestPerceptions(TestPlayableCharacter):
    def test_nothing(self):
        raise Exception('Test not implemented yet')

    def test_wumpus(self):
        raise Exception('Test not implemented yet')

    def test_wumpus_smell(self):
        raise Exception('Test not implemented yet')

    def test_wall(self):
        raise Exception('Test not implemented yet')

    def test_wumpus_yell(self):
        raise Exception('Test not implemented yet')


class TestHunting(TestPlayableCharacter):
    def test_shoot_arrow(self):
        raise Exception('Test not implemented yet')

    def test_shoot_but_no_arrows(self):
        raise Exception('Test not implemented yet')


if __name__ == '__main__':
    unittest.main()
