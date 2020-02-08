from game.src.components.enumerations import Object, Perception
from game.src.engine.action_processor import ActionProcessor


def request_action():
    ap = ActionProcessor()
    action = None
    while action is None:
        print("What is your command?: ")
        command = input()
        action = ap.process_command(command)
        if action is None:
            print("Sorry, I didn't understood you\n")
    return action


def print_board(board, wumpus, player):
    cells = board.cells
    p_x = player.position.x
    p_y = player.position.y
    w_x = wumpus.position.x
    w_y = wumpus.position.y
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
        