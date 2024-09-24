import sys
read = sys.stdin.readline

N = int(read())
coord = [list(map(int, read().split())) for _ in range(N)]
for c in sorted(coord, key=lambda x: (x[1], x[0])):
    print(c[0], c[1])