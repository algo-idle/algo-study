import sys
read = sys.stdin.readline
n = int(read())

memo = [0 for _ in range(50001)]
for i in range(1, n+1):
    memo[i] = memo[i-1] + 1
    j = 1
    while j**2 <= i:
        memo[i] = min(memo[i], memo[i - j**2] + 1)
        j += 1
print(memo[n])