N = int(input())
grid = [0 for _ in range(N)]

res = 0


def can_set(x):
    for i in range(x):
        if grid[x] == grid[i] or abs(grid[x] - grid[i]) == abs(x - i):
            return False
    return True


def backtracking(x):
    global res
    if x == N:
        res += 1
        return
    else:
        for i in range(N):
            grid[x] = i
            if can_set(x):
                backtracking(x + 1)


backtracking(0)
print(res)
