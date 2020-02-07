import unittest

from game.components.playable_character import PlayableCharacter


class TestPlayableCharacter(unittest.TestCase):
    def setUp(self):
        self.pc = PlayableCharacter()

    def test_constructor_default(self):
        self.assertEqual(self.pc.name, "Player")

    def test_constructor_arrows(self):
        pc = PlayableCharacter(arrows=10)
        self.assertEqual(pc.arrows, 10)


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
        arrows = 10
        pc = PlayableCharacter(arrows=arrows)
        for x in range(4):
            arrow = pc.shoot()
            self.assertEqual(pc.arrows, arrows - (x + 1))
            self.assertEqual(arrow.trajectory, pc.position.orientation)
            pc.turn_right()

    def test_shoot_but_no_arrows(self):
        arrow = self.pc.shoot()
        self.assertIsNone(arrow)

class TestExit(TestPlayableCharacter):
    def test_exit_ok(self):
        self.assertTrue(self.pc.exit())

    def test_exit_nok(self):
        self.assertFalse(self.pc.exit())

if __name__ == '__main__':
    unittest.main()
