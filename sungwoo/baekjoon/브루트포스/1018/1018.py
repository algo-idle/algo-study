import sys
read = sys.stdin.readline

N, M = map(int, read().split())
board = [list(str(read().rstrip())) for _ in range(N)]
result = 99999
type = ['W', 'B']

for y in range(N - 7):
    for x in range(M - 7):
        w_start = 0
        b_start = 0
        for i in range(8):
            for j in range(8):
                w = type[(i + j) % 2]
                b = type[(i + j + 1) % 2]

                if board[y + i][x + j] != w:
                    w_start += 1
                if board[y + i][x + j] != b:
                    b_start += 1
        result = min(result, w_start, b_start)

print(result)
