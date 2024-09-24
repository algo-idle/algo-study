import sys
read = sys.stdin.readline

N = int(read())
coord = [list(map(int, read().split())) for _ in range(N)]
for c in sorted(coord):
    print(c[0], c[1])