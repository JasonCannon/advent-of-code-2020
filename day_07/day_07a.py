import sys
from functools import lru_cache

L = [line.strip() for line in sys.stdin]
G = dict()

@lru_cache(maxsize=None)
def contains(u):
    if u == "shiny gold": return True
    return any(contains(v) for n, v in G[u])

for l in L:
    A = l.replace('.', '').replace('no other bags', '').replace('bags', '').replace('bag', '').split('contain')
    C = list(filter(lambda x: x, map(lambda x : x.strip(), ''.join(A[1:]).split(', '))))
    u = A[0].strip()
    G[u] = []
    for c in C:
        n, v = c.split(maxsplit=1)
        G[u].append((int(n), v))

print(sum([contains(u) for u in G])-1)
