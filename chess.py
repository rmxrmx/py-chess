from pprint import pprint
import re
import config
from movement import *
from func import changeTurn
from capture import *


pprint(board)

while True:
    move = input("Input: ")
    if move == "x":
        break

    if re.search(r'^[a-h][1-8]$', move):
        if movePawn(move, config.colour):
            changeTurn()
        else:
            print("Illegal move.")
    # TODO: rework into a switch statement
    elif re.search(r'^[NBRQ][a-h][1-8]-[a-h][1-8]$', move):
        if move[0] == 'N' and moveKnight(move, config.colour) or \
                move[0] == 'B' and moveBishop(move, config.colour) or \
                move[0] == 'R' and moveRook(move, config.colour) or \
                move[0] == 'Q' and moveQueen(move, config.colour):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^K[a-h][1-8]$', move):
        if moveKing(move, config.colour):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^[a-h]x[a-h][1-8]$', move):
        if capturePawn(move, config.colour):
            changeTurn()
        else:
            print("Illegal move.")
    elif re.search(r'^[NBRQK][a-h][1-8]x[a-h][1-8]$', move):
        if move[0] == 'N' and captureKnight(move, config.colour):
            changeTurn()
        else:
            print("Illegal move.")
    # disable enpassant if not used
    if config.colour:
        enpassant[0] = ""
    else:
        enpassant[1] = ""
