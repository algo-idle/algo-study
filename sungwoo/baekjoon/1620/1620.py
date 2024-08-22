import sys
read = sys.stdin.readline

N, M = map(int, read().split())
pokedex = dict()
for i in range(N):
    name = str(read().rstrip())
    pokedex[str(i+1)] = name
    pokedex[name] = i+1

for _ in range(M):
    q = read().rstrip()
    print(pokedex[q])