from config import board, P, p, M, enpassant, N, n
from func import isEmpty
from movement import knightMove


def capturePawn(pos, col):
    y1 = ord(pos[0]) - 97
    x = 8 - int(pos[3])
    y2 = ord(pos[2]) - 97

    if abs(y1 - y2) != 1:
        return False

    if col:
        if board[x + 1][y1] != P:
            print("No pawn")
            return False

        # not a black piece and not en passant
        elif ord(board[x][y2]) < 97 and enpassant[1] != pos[-2:]:
            print("Not capturing a black piece")
            return False

        else:
            board[x + 1][y1] = M
            board[x][y2] = P
            if enpassant[1]:
                board[x + 1][y2] = M

    else:
        if board[x - 1][y1] != p:
            print("No pawn")
            return False

        elif (ord(board[x][y2]) > 90 or isEmpty(x, y2)) and enpassant[0] != pos[-2:]:
            print("Not capturing a white piece")
            return False

        else:
            board[x - 1][y1] = M
            board[x][y2] = p
            if enpassant[0]:
                board[x - 1][y2] = M

    return True


def captureKnight(pos, col):
    # TODO: rework coordinates to reduce code copy/paste
    x1 = 8 - int(pos[2])
    y1 = ord(pos[1]) - 97
    x2 = 8 - int(pos[5])
    y2 = ord(pos[4]) - 97

    if not ((col and board[x1][y1] == N) or (not col and board[x1][y1] == n)):
        print("No knight")
        return False

    if not knightMove(x1, y1, x2, y2):
        return False

    # if not capturing a piece
    if col and ord(board[x2][y2]) < 97 or (not col and (ord(board[x2][y2]) > 90 or isEmpty(x2, y2))):
        return False

    board[x2][y2] = board[x1][y1]
    board[x1][y1] = M
    return True
# TODO: create an isCapturable function, which checks whether the tile given has a piece to be captured
