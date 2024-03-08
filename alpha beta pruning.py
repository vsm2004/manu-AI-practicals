import math
def evaluate(b): return 1 if b == [1, 1, 1] else -1 if b == [-1, -1, -1] else 0
def mmab(b, d, a, B, m):
    if d == 0 or abs(evaluate(b)) == 1: return evaluate(b)
    f = max if m else min
    e = -math.inf if m else math.inf
    for i in range(len(b)):
        if b[i] == 0:
            b[i] = 1 if m else -1
            v = mmab(b, d - 1, a, B, not m)
            b[i], e = 0, f(e, v)
            a = max(a, v) if m else min(a, v)
            if B <= a: break
    return e
board, depth = [0, 0, 0], 3
b, a, B = -1, -math.inf, math.inf
print("Best move:", max(((i, mmab(board[:], depth, a, B, False)) for i in range(len(board)) if board[i] == 0), key=lambda x: x[1])[0])
