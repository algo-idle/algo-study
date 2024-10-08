import sys

read = sys.stdin.readline

N = int(read())
paper = [list(map(int, read().split())) for _ in range(N)]

white_square, blue_square = 0, 0


def cal_square(x, y, n):
    global white_square, blue_square
    count = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[j][i]:
                count += 1
    if not count:
        white_square += 1
    elif count == n ** 2:
        blue_square += 1
    else:
        cal_square(x, y, n // 2)
        cal_square(x + n // 2, y, n // 2)
        cal_square(x, y + n // 2, n // 2)
        cal_square(x + n // 2, y + n // 2, n // 2)


cal_square(0, 0, N)
print(white_square, blue_square, sep='\n')
