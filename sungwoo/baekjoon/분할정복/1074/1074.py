import sys
read = sys.stdin.readline

N, r, c = map(int, read().split())

n = 2 ** (N-1)
result = 0
while 1 <= N:
    if r / n < 1 and c / n < 1:
        result += 0
    elif r / n < 1 and c / n >= 1:
        result += (2 ** (N-1)) ** 2
        c -= n
    elif r / n >= 1 and c / n < 1:
        result += (2 ** (N-1)) ** 2 * 2
        r -= n
    else:
        result += (2 ** (N-1)) ** 2 * 3
        r -= n
        c -= n
    N -= 1
    n /= 2

print(result)