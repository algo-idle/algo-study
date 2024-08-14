import sys
import math
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    M, N, x, y = map(int, read().split())
    candidate_number = []
    lcm = math.lcm(M, N)
    isFound = False
    for i in range(int(lcm/M)):
        candidate_number.append(M * i + x)
    for i in candidate_number:
        if (i - y) % N == 0:
            isFound = True
            print(i)
            break
    if not isFound:
        print(-1)