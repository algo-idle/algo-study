import sys

read = sys.stdin.readline
N = int(read())
time = list(map(int, read().split()))
time.sort()
total = 0
for i in range(N):
    total += (N - i) * time[i]
print(total)