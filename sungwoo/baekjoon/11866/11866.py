import sys
read = sys.stdin.readline

N, K = map(int, read().split())
queue = []
for i in range(N):
    queue.append(i+1)
cursor = 0
print('<', end='')
while queue:
    cursor = (cursor + K - 1) % N
    N -= 1
    print(queue.pop(cursor), end='')
    if queue:
        print(', ', end='')
    else:
        print('>')
