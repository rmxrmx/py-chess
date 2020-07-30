from pprint import pprint
import re

# White = uppercase, black = lowercase
R = 'R'
N = 'N'
B = 'B'
Q = 'Q'
K = 'K'
P = 'P'
r = 'r'
n = 'n'
b = 'b'
q = 'q'
k = 'k'
p = 'p'
M = "."

board = [[r, n, b, q, k, b, n, r],
         [p, p, p, p, p, p, p, p],
         [M, M, M, M, M, M, M, M],
         [M, M, M, M, M, M, M, M],
         [M, M, M, M, M, M, M, M],
         [M, M, M, M, M, M, M, M],
         [P, P, P, P, P, P, P, P],
         [R, N, B, Q, K, B, N, R]]
colour = True


def changeTurn():
    global colour
    pprint(board)
    colour = not colour


# check whether tile is empty
def isEmpty(x, y):
    if board[x][y] != M:
        print("Not empty")
        return False
    return True


# check if the position given can be moved to by the queen
def queenMove(x1, y1, x2, y2):
    # bishop-like
    if abs(x1 - x2) == abs(y1 - y2) and x1 != x2:
        return True
    # rook-like
    elif x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2:
        return True
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


def movePawn(pos, col):
    # convert position to array-like
    x = 8 - int(pos[1])
    y = ord(pos[0]) - 97

    if not isEmpty(x, y):
        return False

    if col:
        print("White")
        if board[x + 1][y] == P:
            board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
            return True
        # TODO: implement en passant mechanics
        elif x == 4 and board[x + 2][y] == P and isEmpty(x + 1, y):
            board[x][y], board[x + 2][y] = board[x + 2][y], board[x][y]
            return True
    else:
        print("Black")
        if board[x - 1][y] == p:
            board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
            return True
        # TODO: implement en passant mechanics
        elif x == 3 and board[x - 2][y] == p and isEmpty(x - 1, y):
            board[x][y], board[x - 2][y] = board[x - 2][y], board[x][y]
            return True
    return False


def moveKnight(pos, col):
    # TODO: rework coordinates to reduce code copy/paste
    x1 = 8 - int(pos[2])
    y1 = ord(pos[1]) - 97
    x2 = 8 - int(pos[5])
    y2 = ord(pos[4]) - 97

    if not ((col and board[x1][y1] == N) or (not col and board[x1][y1] == n)):
        print("No knight")
        return False

    if not (abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
        print("Not a knight move")
        return False

    if not isEmpty(x2, y2):
        return False

    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
    return True


def moveBishop(pos, col):
    x1 = 8 - int(pos[2])
    y1 = ord(pos[1]) - 97
    x2 = 8 - int(pos[5])
    y2 = ord(pos[4]) - 97

    if not ((col and board[x1][y1] == B) or (not col and board[x1][y1] == b)):
        print("No bishop")
        return False

    if not (abs(x1 - x2) == abs(y1 - y2) and x1 != x2):
        print("Not a bishop move")
        return False

    return checkPath(x1, y1, x2, y2)


def moveRook(pos, col):
    x1 = 8 - int(pos[2])
    y1 = ord(pos[1]) - 97
    x2 = 8 - int(pos[5])
    y2 = ord(pos[4]) - 97

    if not ((col and board[x1][y1] == R) or (not col and board[x1][y1] == r)):
        print("No rook")
        return False

    if not (x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2):
        print("Not a rook move")
        return False

    return checkPath(x1, y1, x2, y2)


def moveQueen(pos, col):
    x1 = 8 - int(pos[2])
    y1 = ord(pos[1]) - 97
    x2 = 8 - int(pos[5])
    y2 = ord(pos[4]) - 97

    if not ((col and board[x1][y1] == Q) or (not col and board[x1][y1] == q)):
        print("No Queen")
        return False

    if not queenMove(x1, y1, x2, y2):
        print("Not a Queen move")
        return False

    return checkPath(x1, y1, x2, y2)


# TODO: avoid check when moving
# TODO: implement castling
def moveKing(pos, col):
    x = 8 - int(pos[2])
    y = ord(pos[1]) - 97

    if not isEmpty(x, y):
        return False

    # check for king within the spaces
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (0 <= x + i, y + j <= 7) and (
                    (col and board[x + i][y + j] == K) or (not col and board[x + i][y + j] == k)):
                board[x][y], board[x + i][y + j] = board[x + i][y + j], board[x][y]
                return True
    return False


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


pprint(board)

while True:
    move = input("Input: ")
    if move == "x":
        break

    if re.search(r'^[a-h][1-8]$', move):
        if movePawn(move, colour):
            changeTurn()
        else:
            print("Illegal move.")
    # TODO: rework into a switch statement
    elif re.search(r'^[NBRQ][a-h][1-8]-[a-h][1-8]$', move):
        if move[0] == 'N' and moveKnight(move, colour) or \
                move[0] == 'B' and moveBishop(move, colour) or \
                move[0] == 'R' and moveRook(move, colour) or \
                move[0] == 'Q' and moveQueen(move, colour):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^K[a-h][1-8]$', move):
        if moveKing(move, colour):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^[a-h]x[a-h][1-8]$', move):
        if capturePawn(move, colour):
            changeTurn()
        else:
            print("Illegal move.")
