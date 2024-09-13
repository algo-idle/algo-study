import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

x, y = len(B), len(A)
res = ''
while dp[x][y] != 0:
    if dp[x - 1][y] == dp[x][y]:
        x -= 1
    elif dp[x][y - 1] == dp[x][y]:
        y -= 1
    else:
        res += B[x - 1]
        x -= 1
        y -= 1

print(dp[-1][-1])
print(''.join(list(reversed(res))))

