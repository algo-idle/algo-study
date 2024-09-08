import sys
input = sys.stdin.readline

N = int(input().rstrip())
c = [list(map(int, input().rstrip().split())) for _ in range(N)]
c.append(c[0])

print(round(0.5*(abs(sum([c[i][0] * c[i + 1][1] for i in range(N)]) - sum([c[i][1] * c[i + 1][0] for i in range(N)]))), 1))