import numpy as np

R = "wrook"
N = "wknight"
B = "wbishop"
Q = "wqueen"
K = "wking"
P = "wpawn"
r = "brook"
n = "bknight"
b = "bbishop"
q = "bqueen"
k = "bking"
p = "bpawn"

board = np.array([[r, n, b, q, k, b, n, r],
                 [p, p, p, p, p, p, p, p],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [P, P, P, P, P, P, P, P],
                 [R, N, B, Q, K, B, N, R]])

"""
while True:
    ip = input("Input: ")
    if ip == "x":
        break
"""