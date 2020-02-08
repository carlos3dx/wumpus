from copy import deepcopy

from game.src.components.arrow import Arrow
from game.src.components.board import Board
from game.src.components.character import Character
from game.src.components.enumerations import Actions
from game.src.components.game import Game


def process_shoot(game: Game, arrow: Arrow):
    refresh = False
    if arrow is not None and game.wumpus is not None:
        print("An arrow was shoot from your bow")
        w_x = game.wumpus.position.x
        w_y = game.wumpus.position.y
        p_x = game.player.position.x
        p_y = game.player.position.y

        # check oorientation from player to wumpus
        if p_x == w_x or p_y == w_y:
            if p_x == w_x:
                if p_y > w_y:
                    relative_position = 2
                else:
                    relative_position = 0
            else:
                if p_x > w_x:
                    relative_position = 3
                else:
                    relative_position = 1
            if relative_position == arrow.trajectory:
                print("You perceive the Wumpus yelling in agony, you killed it")
                game.player.kill_wumpus()
                game.wumpus = None
                refresh = True
    return refresh


def move(character: Character, board: Board):
    pos = deepcopy(character.position)
    pos.move_forward()
    if len(board.cells) <= pos.y and len(board.cells[0]) <= pos.x:
        print("Cannot move through walls")
        refresh = False
    else:
        character.move_forward()
        refresh = True
    return refresh


def check_exit(game):
    player = game.player
    if player.position.x == 0 and player.position.y == 0:
        gold = player.has_gold
        wumpus = player.killed_wumpus

        if gold and wumpus:
            print("Congratulations, you managed to kill the Wumpus, collect the gold and getting out.")
        elif gold:
            print(
                "Congratulations, you managed to collect the gold and getting out without risking your life with the Wumpus.")
        elif wumpus:
            print("Contratulations hunter, you killed the Wumpus and returned to your home.")
        else:
            print("You returned home without the gold or the Wumpus head")
        exit(0)
    else:
        print("There is no exit here, you should go to the entrance")


def process_actions_player(game: Game, action: Actions):
    refresh = False
    if action == Actions.MOVE:
        refresh = move(game.player, game.board)
    elif action == Actions.TURN_LEFT:
        game.player.turn_left()
    elif action == Actions.TURN_RIGHT:
        game.player.turn_right()
    elif action == Actions.SHOOT:
        arrow = game.player.shoot()
        refresh = process_shoot(game, arrow)
    elif action == Actions.EXIT:
        check_exit(game)
    return refresh

