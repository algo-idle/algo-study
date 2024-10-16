import sys
read = sys.stdin.readline

n = int(read())
stairs = [int(read()) for _ in range(n)]

if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
else:
    memo = [0] * (n + 1)
    memo[1] = stairs[0]
    memo[2] = stairs[0] + stairs[1]

    for i in range(3, n+1):
        memo[i] = max(memo[i-2]+stairs[i-1], memo[i-3]+stairs[i-2]+stairs[i-1])
    print(memo[-1])