import sys
read = sys.stdin.readline

N, K = map(int, read().split())
baggage = [list(map(int, read().split())) for _ in range(N)]

table = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if baggage[i-1][0] > j:
            table[i][j] = table[i-1][j]
        else:
            with_value = baggage[i-1][1] + table[i-1][j - baggage[i-1][0]]
            without_value = table[i-1][j]
            table[i][j] = max(with_value, without_value)

print(table[N][K])