import config
from pprint import pprint


def changeTurn():
    pprint(config.board)
    config.colour = not config.colour


# check whether tile is empty
def isEmpty(x, y):
    if config.board[x][y] != config.M:
        print("Not empty")
        return False
    return True
