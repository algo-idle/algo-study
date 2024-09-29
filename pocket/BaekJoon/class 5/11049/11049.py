import sys
input = sys.stdin.readline

N = int(input().rstrip())
mat = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for term in range(1, N):
    for start in range(N - term):
        dp[start][start + term] = int(1e10)

        for i in range(start, start + term):
            dp[start][start + term] = min(dp[start][start + term],
                                          dp[start][i] + dp[i + 1][start + term] + (mat[start][0] * mat[i][1] * mat[start + term][1]))

print(dp[0][-1])
