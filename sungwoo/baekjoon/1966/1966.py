import sys
read = sys.stdin.readline
from collections import deque

T = int(read())
for _ in range(T):
    N, M = map(int, read().split())
    docs = list(map(int, read().split()))
    queue = deque()
    count = 0
    for i in range(len(docs)):
        queue.append((docs[i], i))
    while queue:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())