import sys

def get_id(s):
    row = int(s[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(s[7:].replace('R', '1').replace('L', '0'), 2)
    return 8*row + col

L = [line.strip() for line in sys.stdin]

print(max([get_id(l) for l in L]))
