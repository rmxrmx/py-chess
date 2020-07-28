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

board = [[r, n, b, q, k, b, n, r],
         [p, p, p, p, p, p, p, p],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [P, P, P, P, P, P, P, P],
         [R, N, B, Q, K, B, N, R]]

colour = True


def movePawn(pos, col):
    # convert position to array-like
    y = ord(pos[0]) - 97
    x = 8 - int(pos[1])

    if board[x][y] != 0:
        print("Not empty")
        return False
    if col:
        print("White")
        if board[x+1][y] == P:
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
            return True
        # TODO: implement en passant mechanics
        elif x == 4 and board[x+2][y] == P:
            board[x][y], board[x+2][y] = board[x+2][y], board[x][y]
            return True
    else:
        print("Black")
        if board[x-1][y] == p:
            board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
            return True
        # TODO: implement en passant mechanics
        elif x == 3 and board[x-2][y] == P:
            board[x][y], board[x-2][y] = board[x-2][y], board[x][y]
            return True
    return False


while True:
    move = input("Input: ")
    if move == "x":
        break
    if re.search(r'[a-h][1-8]', move):
        if not movePawn(move, colour):
            print("Illegal move.")
        else:
            pprint(board)
            colour = not colour
