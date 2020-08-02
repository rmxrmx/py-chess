from func import isEmpty, isPiece
from config import board, P, N, B, R, Q, K, enpassant
import config


# check if the position given can be moved to by the queen
def queenMove(x1, y1, x2, y2):
    # bishop-like
    if abs(x1 - x2) == abs(y1 - y2) and x1 != x2:
        return True
    # rook-like
    elif x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2:
        return True
    print("Not a queen move")
    return False


def knightMove(x1, y1, x2, y2):
    if abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
        return True
    print("Not a knight move")
    return False


def bishopMove(x1, y1, x2, y2):
    if not (abs(x1 - x2) == abs(y1 - y2) and x1 != x2):
        print("Not a bishop move")
        return False


# checks that the path of the figure is clear
def checkPath(x1, y1, x2, y2):
    tx = x2
    ty = y2

    # check every cell along the way
    while x1 != tx or y1 != ty:
        print(tx, ty)
        if not isEmpty(tx, ty):
            print("Can't move there")
            return False
        if tx < x1:
            tx += 1
        elif tx > x1:
            tx -= 1
        if ty < y1:
            ty += 1
        elif ty > y1:
            ty -= 1

    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
    return True


def movePawn(pos):
    # convert position to array-like
    x = 8 - int(pos[1])
    y = ord(pos[0]) - 97

    if not isEmpty(x, y):
        return False

    if config.colour:
        print("White")
        if isPiece(x + 1, y, P):
            board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
            return True

        # en passant mechanics
        elif x == 4 and isPiece(x + 2, y, P) and isEmpty(x + 1, y):
            board[x][y], board[x + 2][y] = board[x + 2][y], board[x][y]
            enpassant[0] = pos[0] + str(int(pos[1]) - 1)
            return True
    else:
        print("Black")
        if isPiece(x - 1, y, P):
            board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
            return True

        # en passant mechanics
        elif x == 3 and isPiece(x - 2, y, P) and isEmpty(x - 1, y):
            board[x][y], board[x - 2][y] = board[x - 2][y], board[x][y]
            enpassant[1] = pos[0] + str(int(pos[1]) + 1)
            return True

    return False


def moveKnight(x1, y1, x2, y2):

    if not isPiece(x1, y1, N):
        print("No knight")
        return False

    if not knightMove(x1, y1, x2, y2):
        return False

    if not isEmpty(x2, y2):
        return False

    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
    return True


def moveBishop(x1, y1, x2, y2):

    if not isPiece(x1, y1, B):
        print("No bishop")
        return False

    if not (abs(x1 - x2) == abs(y1 - y2) and x1 != x2):
        print("Not a bishop move")
        return False

    return checkPath(x1, y1, x2, y2)


def moveRook(x1, y1, x2, y2):

    if not isPiece(x1, y1, R):
        print("No rook")
        return False

    if not (x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2):
        print("Not a rook move")
        return False

    return checkPath(x1, y1, x2, y2)


def moveQueen(x1, y1, x2, y2):

    if not isPiece(x1, y1, Q):
        print("No Queen")
        return False

    if not queenMove(x1, y1, x2, y2):
        print("Not a Queen move")
        return False

    return checkPath(x1, y1, x2, y2)
# TODO: rework movement into a single function move(x1, y1, x2, y2, PIECE)


# TODO: avoid check when moving
# TODO: implement castling
def moveKing(pos):
    x = 8 - int(pos[2])
    y = ord(pos[1]) - 97

    if not isEmpty(x, y):
        return False

    # check for king within the spaces
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (0 <= x + i <= 7 and 0 <= y + j <= 7) and isPiece(x + i, y + j, K):
                board[x][y], board[x + i][y + j] = board[x + i][y + j], board[x][y]
                return True
    return False
