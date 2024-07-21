import sys

read = sys.stdin.readline
T = int(read())

for _ in range(T):
    N = int(read())
    if N == 0:
        print("1 0")
        continue
    table = [0 for _ in range(N + 1)]
    for i in range(0, N+1):
        if i == 0:
            table[i] = 0
        elif i == 1:
            table[i] = 1
        else:
            table[i] = table[i - 1] + table[i - 2]
    print(table[N-1], table[N])