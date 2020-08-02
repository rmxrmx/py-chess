import config
from config import board, enpassant, M, P, p, N
from func import isPiece
from movement import knightMove


# check whether the piece on the tile can be captured
def isCapturable(x, y):
    if config.colour:
        if 97 <= ord(board[x][y]) <= 122:
            return True
    else:
        if 65 <= ord(board[x][y]) <= 90:
            return True
    return False


def capturePawn(pos):
    y1 = ord(pos[0]) - 97
    x = 8 - int(pos[3])
    y2 = ord(pos[2]) - 97

    if abs(y1 - y2) != 1:
        return False

    if config.colour:
        if not isPiece(x + 1, y1, P):
            print("No pawn")
            return False

        # not a black piece and not en passant
        elif not isCapturable(x, y2) and enpassant[1] != pos[-2:]:
            print("Not capturing a black piece")
            return False

        else:
            board[x + 1][y1] = M
            board[x][y2] = P
            if enpassant[1]:
                board[x + 1][y2] = M

    else:
        if not isPiece(x - 1, y1, P):
            print("No pawn")
            return False

        elif not isCapturable(x, y2) and enpassant[0] != pos[-2:]:
            print("Not capturing a white piece")
            return False

        else:
            board[x - 1][y1] = M
            board[x][y2] = p
            if enpassant[0]:
                board[x - 1][y2] = M

    return True


def captureKnight(x1, y1, x2, y2):
    # TODO: rework coordinates to reduce code copy/paste

    if not isPiece(x1, y1, N):
        print("No knight")
        return False

    if not knightMove(x1, y1, x2, y2):
        return False

    # if not capturing a piece
    if not isCapturable(x2, y2):
        return False

    board[x2][y2] = board[x1][y1]
    board[x1][y1] = M
    return True
