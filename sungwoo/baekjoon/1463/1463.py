import sys
read = sys.stdin.readline

N = int(read())
memo = [0] * (N + 1)
pos = 2
while pos < N + 1:
    memo[pos] = memo[pos - 1] + 1
    if pos % 2 == 0:
        memo[pos] = min(memo[pos], memo[pos // 2] + 1)
    if pos % 3 == 0:
        memo[pos] = min(memo[pos], memo[pos // 3] + 1)
    pos += 1
print(memo[N])