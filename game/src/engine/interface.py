from game.src.components.enumerations import Object, Perception
from game.src.engine.command_processor import CommandProcessor


def request_action():
    ap = CommandProcessor()
    action = None
    while action is None:
        print("What is your command?: ")
        command = input()
        action = ap.process_command(command)
        if action is None:
            print("Sorry, I didn't understood you\n")
    return action


def print_board(game):
    cells = game.board.cells
    p_x = game.player.position.x
    p_y = game.player.position.y
    if game.wumpus is None:
        w_x = -1
        w_y = -1
    else:
        w_x = game.wumpus.position.x
        w_y = game.wumpus.position.y
    for i in range(len(cells)-1, -1, -1):
        row = cells[i]
        chars = []
        for j in range(len(row)):
            cell = row[j]
            if p_x == j and p_y == i:
                char = "P"
            elif w_x == j and w_y == i:
                char = "W"
            elif cell.object == Object.GOLD:
                char = "G"
            elif cell.object == Object.PIT:
                char = "O"
            elif Perception.BREEZE in cell.perceptions:
                char = "b"
            elif Perception.WUMPUS_ODOR in cell.perceptions:
                char = "o"
            elif Perception.WALL in cell.perceptions:
                char = "w"
            else:
                char = " "
            chars.append(char)
        line = "|".join(chars)
        print(f'|{line}|')
