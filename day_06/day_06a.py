import sys
from functools import reduce

L, Q = [line.strip() for line in sys.stdin], []
sm = 0

for l in L + ['']:
    if l != '':
        Q.append(l)
        continue
    sm += len(reduce(lambda a, b: set(a) | set(b), Q))
    Q = []

print(sm)
