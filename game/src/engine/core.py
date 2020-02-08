# Expect user input
#  Do action
# Process result
#  Update
from game.src.components.game import Game
from game.src.components.playable_character import PlayableCharacter
from game.src.components.wumpus import Wumpus
from game.src.engine.action_processor import process_actions_player
from game.src.engine.board_utils import create_board, refresh_board, check_pit
from game.src.engine.interface import request_action, print_board
from game.src.components.position import Position
from game.src.engine.perceptions_processor import evaluate_perceptions


def play(x, y, pits, arrows, debug):
    game = setUp(x, y, pits, arrows)
    core(game, debug)


def setUp(x, y, pits, arrows):
    player = PlayableCharacter(arrows=arrows)
    wumpus = Wumpus()
    board = create_board(x, y, pits, wumpus)
    return Game(board, wumpus, player)


def core(game, debug):
    finished = False
    while not finished:
        if debug:
            print_debug(game)
        evaluate_perceptions(game)
        action = request_action()
        check_pit(game)
        if process_actions_player(game, action):
            refresh_board(game)



def print_debug(game):
    print_board(game)
    orientation = Position.directions[game.player.position.orientation]
    print(f'The player is facing {orientation} and has {game.player.arrows} arrows')
