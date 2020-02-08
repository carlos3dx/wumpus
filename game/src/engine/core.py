# Expect user input
#  Do action
# Process result
#  Update
from game.src.components.playable_character import PlayableCharacter
from game.src.components.wumpus import Wumpus
from game.src.engine.init_board import create_board
from game.src.engine.interface import request_action, print_board
from game.src.components.position import Position


def play(x, y, pits, arrows, debug):
    player, wumpus, board = setUp(x, y, pits, arrows)
    core(player, wumpus, board, debug)


def setUp(x, y, pits, arrows):
    player = PlayableCharacter(arrows=arrows)
    wumpus = Wumpus()
    board = create_board(x, y, pits, wumpus)
    return player, wumpus, board


def core(player, wumpus, board, debug):
    finished = False
    while not finished:
        if debug:
            print_debug(board, wumpus, player)
        action = request_action()


def print_debug(board, wumpus, player):
    print_board(board, wumpus, player)
    orientation = Position.directions[player.position.orientation]
    print(f'The player is facing {orientation} and has {player.arrows} arrows')