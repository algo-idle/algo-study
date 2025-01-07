import sys
read = sys.stdin.readline

N = int(read())

prev = 1
curr = 1

for _ in range(N-1):
    tmp = prev
    prev = curr
    curr = (curr + tmp) % 15746

print(curr)