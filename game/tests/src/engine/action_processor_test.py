import unittest

from game.src.components.enumerations import Actions
from game.src.engine.action_processor import ActionProcessor


class TestActionProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ActionProcessor()


class TestMovement(TestActionProcessor):
    ok_commands = ["move", "move forward", "move forwards"]
    nok_commands = ["forward move", "move backwards", "move_forward", "nonsense"]

    def test_move_ok(self):
        for x in self.ok_commands:
            self.assertEqual(self.processor.process_command(x), Actions.MOVE, "An action movement should be returned")

    def test_move_nok(self):
        for x in self.nok_commands:
            self.assertIsNone(self.processor.process_command(x), "'None' should be returned")


class TestTurn(TestActionProcessor):
    ok_commands_left = ["turn left", "left turn"]
    ok_commands_right = ["turn right", "right turn"]
    nok_commands = ["turn", "right left turn", "right turn right", "turn up", "turn down", "turn left turn"]

    def test_turn_left(self):
        for x in self.ok_commands_left:
            self.assertEqual(self.processor.process_command(x), Actions.TURN_LEFT,
                             "A left turn action should be returned")

    def test_turn_right(self):
        for x in self.ok_commands_right:
            self.assertEqual(self.processor.process_command(x), Actions.TURN_RIGHT,
                             "A right turn action should be returned")

    def test_move_nok(self):
        for x in self.nok_commands:
            self.assertIsNone(self.processor.process_command(x), "'None' should be returned")


class TestShoot(TestActionProcessor):
    ok_commands = ["shoot", "shoot arrow", "throw arrow"]
    nok_commands = ["throw", "shoot throw", "throw shoot", "throw shoot arrow", "kill"]

    def test_shoot_ok(self):
        for x in self.ok_commands:
            self.assertEqual(self.processor.process_command(x), Actions.SHOOT, "A shoot action should be returned")

    def test_shoot_nok(self):
        for x in self.nok_commands:
            self.assertIsNone(self.processor.process_command(x), "'None' should be returned")


class TestExit(TestActionProcessor):
    ok_commands = ["exit", "exit board", "exit game", "go outside"]
    nok_commands = ["exit nonsense", "go inside", "exit outside"]

    def test_exit_ok(self):
        for x in self.ok_commands:
            self.assertEqual(self.processor.process_command(x), Actions.EXIT, "An exit action should be returned")

    def test_exit_nok(self):
        for x in self.nok_commands:
            self.assertIsNone(self.processor.process_command(x), "'None' should be returned")


if __name__ == '__main__':
    unittest.main()
