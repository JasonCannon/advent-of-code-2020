import sys

D = set()
for line in sys.stdin:
    a = int(line)
    if a in D:
        print(a*(2020-a))
    D.add(2020-a)