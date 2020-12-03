import sys


def count(I, i, j):
    r, c, cnt = 0, 0, 0
    
    while True:
        r += i
        c = (c+j) % len(I[0])
        if r >= len(I): break
        cnt += I[r][c] == '#'

    return cnt

if __name__ == "__main__":
    I = [line.strip() for line in sys.stdin]
    print(count(I, 1, 1)*count(I, 1, 3)*count(I, 1, 5)*count(I, 1, 7)*count(I, 2, 1))