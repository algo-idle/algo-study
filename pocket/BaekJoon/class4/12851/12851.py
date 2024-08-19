from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
q = deque([N])
visited[N] = 1
cnt = 0

while q:
    pos = q.popleft()
    if pos == K:
        cnt += 1
    else:
        for new_pos in [pos + 1, pos - 1, pos * 2]:
            if 0 <= new_pos <= 100000:
                if visited[new_pos] == 0:
                    visited[new_pos] = visited[pos] + 1
                    q.append(new_pos)
                elif visited[new_pos] == visited[pos] + 1:
                    q.append(new_pos)

print(visited[K] - 1)
print(cnt)
