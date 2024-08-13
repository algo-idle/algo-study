import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

N = int(input().rstrip())
grid = [[' ' for _ in range((N * 2) - 1)] for _ in range(N)]

def print_star(x, y, n):
    if n == 3:
        grid[x - 2][y - 2] = '*'
        for d in [-3, -1]:
            grid[x - 1][y + d] = '*'
        for d in [-4, -3, -2, -1, 0]:
            grid[x][y + d] = '*'
    else:
        print_star(x, y, n // 2)
        print_star(x - (n // 2), y - (n // 2), n // 2)
        print_star(x, y - n, n // 2)

print_star(N - 1, (N * 2) - 2, N)
for g in grid:
    print(''.join(g))
