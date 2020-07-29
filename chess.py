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


# check whether tile is empty
def isEmpty(x, y):
    if board[x][y] != M:
        return False
    return True


def movePawn(pos, col):
    # convert position to array-like
    x = 8 - int(pos[1])
    y = ord(pos[0]) - 97

    if not isEmpty(x, y):
        print("Not empty")
        return False
    if col:
        print("White")
        if board[x + 1][y] == P:
            board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
            return True
        # TODO: implement en passant mechanics
        elif x == 4 and board[x + 2][y] == P:
            board[x][y], board[x + 2][y] = board[x + 2][y], board[x][y]
            return True
    else:
        print("Black")
        if board[x - 1][y] == p:
            board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
            return True
        # TODO: implement en passant mechanics
        elif x == 3 and board[x - 2][y] == P:
            board[x][y], board[x - 2][y] = board[x - 2][y], board[x][y]
            return True
    return False


def moveKnight(pos, col):
    x1 = 8 - int(pos[2])
    y1 = ord(pos[1]) - 97
    x2 = 8 - int(pos[5])
    y2 = ord(pos[4]) - 97

    if not (abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
        print("Not a knight move")
        return False

    if not isEmpty(x2, y2):
        print("Not empty")
        return False

    if (col and board[x1][y1] == N) or (not col and board[x1][y1] == n):
        board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
        return True
    return False


while True:
    move = input("Input: ")
    if move == "x":
        break
    if re.search(r'^[a-h][1-8]$', move):
        if not movePawn(move, colour):
            print("Illegal move.")
        else:
            pprint(board)
            colour = not colour

    elif re.search(r'^N[a-h][1-8]-[a-h][1-8]$', move):
        if not moveKnight(move, colour):
            print("Illegal move.")
        else:
            pprint(board)
            colour = not colour
