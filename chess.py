from pprint import pprint
import re
from movement import *
from func import changeTurn
from capture import *


pprint(board)

while True:
    move = input("Input: ")
    if move == "x":
        break

    if re.search(r'^[a-h][1-8]$', move):
        if movePawn(move):
            changeTurn()
        else:
            print("Illegal move.")
    # TODO: rework into a switch statement
    elif re.search(r'^[NBRQ][a-h][1-8]-[a-h][1-8]$', move):
        x1 = 8 - int(move[2])
        y1 = ord(move[1]) - 97
        x2 = 8 - int(move[5])
        y2 = ord(move[4]) - 97

        if move[0] == 'N' and moveKnight(x1, y1, x2, y2) or \
                move[0] == 'B' and moveBishop(x1, y1, x2, y2) or \
                move[0] == 'R' and moveRook(x1, y1, x2, y2) or \
                move[0] == 'Q' and moveQueen(x1, y1, x2, y2):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^K[a-h][1-8]$', move):
        if moveKing(move):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^[a-h]x[a-h][1-8]$', move):
        if capturePawn(move):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^[NBRQK][a-h][1-8]x[a-h][1-8]$', move):
        x1 = 8 - int(move[2])
        y1 = ord(move[1]) - 97
        x2 = 8 - int(move[5])
        y2 = ord(move[4]) - 97

        if move[0] == 'N' and captureKnight(x1, y1, x2, y2):
            changeTurn()
        else:
            print("Illegal move.")
    # disable enpassant if not used
    if config.colour:
        enpassant[0] = ""
    else:
        enpassant[1] = ""
