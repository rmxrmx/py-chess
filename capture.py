from func import isEmpty
from config import board, P, p, M


def capturePawn(pos, col):
    y1 = ord(pos[0]) - 97
    x = 8 - int(pos[3])
    y2 = ord(pos[2]) - 97

    if abs(y1 - y2) != 1:
        return False

    if isEmpty(x, y2):
        return False

    if col:
        if board[x + 1][y1] != P:
            print("No pawn")
            print(x + 1, y1)
            return False
        # not a black piece
        elif ord(board[x][y2]) < 97:
            print("Not capturing a black piece")
            return False
        else:
            board[x + 1][y1] = M
            board[x][y2] = P
    else:
        if board[x - 1][y1] != p:
            print("No pawn")
            return False
        elif ord(board[x][y2]) > 90:
            print("Not capturing a white piece")
            return False
        else:
            board[x - 1][y1] = M
            board[x][y2] = p
    return True
