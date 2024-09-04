import sys
from collections import deque
read = sys.stdin.readline


T = int(read())
for _ in range(T):
    x = list(read().rstrip())
    queue = deque()
    for i in x:
        if i == '(':
            queue.append(i)
        elif queue:
            queue.popleft()
        else:
            queue.append(i)
            break
    print('NO' if queue else 'YES')