import sys

L = [int(line) for line in sys.stdin]
D = set(l for l in L)

for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if 2020-L[i]-L[j] in D:
            print(L[i]*L[j]*(2020-L[i]-L[j]))
            sys.exit(0)