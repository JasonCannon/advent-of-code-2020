import sys

cnt = 0

for line in sys.stdin:
    nums, c, s = line.split()
    n, m = map(int, nums.split('-'))
    cnt += n <= s.count(c[0]) <= m

print(cnt)
