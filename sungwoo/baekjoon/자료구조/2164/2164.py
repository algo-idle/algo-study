import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
queue = deque(i + 1 for i in range(N))
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])
