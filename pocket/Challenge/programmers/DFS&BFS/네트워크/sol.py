from collections import deque


def solution(n, computers):
    visited = [0 for _ in range(n)]

    def bfs(start):

        q = deque([start])

        visited[start] = 1

        while q:

            x = q.popleft()

            for i in range(n):

                if computers[x][i] == 1 and visited[i] == 0:
                    q.append(i)

                    visited[i] = 1

    answer = 0

    for i in range(n):

        if not visited[i]:
            print(visited, i)
            bfs(i)

            answer += 1

    return answer