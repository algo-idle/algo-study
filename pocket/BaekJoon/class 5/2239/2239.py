import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
zeros.sort(reverse=True)

def get_possible(x, y):
    possible = [i for i in range(1, 10)]
    for i in range(0, 9):
        if board[i][y] != 0:
            possible[board[i][y] - 1] = 0
        if board[x][i] != 0:
            possible[board[x][i] - 1] = 0

    start_x, start_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if board[i][j] != 0:
                possible[board[i][j] - 1] = 0

    return [p for p in possible if p != 0]

def sudoku():
    global board

    if zeros:
        x, y = zeros.pop()
    else:
        for b in board:
            print(''.join(str(_b) for _b in b))
        exit(0)

    possible = get_possible(x, y)
    for p in possible:
        board[x][y] = p
        sudoku()
        board[x][y] = 0

    zeros.append((x, y))

sudoku()
