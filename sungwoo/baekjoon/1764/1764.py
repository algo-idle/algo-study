import sys

read = sys.stdin.readline
N, M = map(int, read().split())
not_hear = set(str(read().strip()) for _ in range(N))
not_see = set(str(read().strip()) for _ in range(M))
not_hear_and_see = sorted(not_hear & not_see)
print(len(not_hear_and_see))
for p in not_hear_and_see:
    print(p)