import sys

cnt = 0

for line in sys.stdin:
    nums, c, s = line.split()
    n, m = map(int, nums.split('-'))
    cnt += (s[n-1] == c[0]) + (s[m-1] == c[0]) == 1

print(cnt)
